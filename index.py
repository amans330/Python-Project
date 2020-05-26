from tkinter import *
import webbrowser
import urllib.request
import json
from tkinter import messagebox
from datetime import datetime

base_url = 'https://developer.trimet.org/ws/v2/arrivals?'
find_stations_url = 'https://trimet.org/ride/stop_select_form.html'
appID = 'appID=294B60BEC29C4DEBD3D8A96AB'

def open_station_browser():
	''' Opens the web page to find station id for any location
		The API for finding station id from address is not available
		and not exposed by trimet. The user will use this station id to search for arrivals data
	'''
	webbrowser.open_new(find_stations_url)

def open_readme():
	messagebox.showinfo("How to Use this App", 'Welcome to the Trimet Arrivals Information App!'+
		'\n\nThis application shows you all upcoming arrivals for any stop for the duration provided by '
		'the user in minutes. \n\nIf you need help finding your stop id, click on help and visit the trimet '
		'website. Enter the name of your stop to know its stop id.\n\nThe stop id takes only numbers and '
		'is mandatory.\n\nThe duration is in minutes and can be left blank. In that case the default value '
		'would be 20 minutes. The max duration trimet supports is 60 minutes. \n\nThe App also shows you '
		'updated arrival status for each arrival and will let you know how much is it late.\n\n'+
		'The results window will also show the name of the station so you can be sure that you are searching '
		'for the right station.\n\nThis App also supports streetcar arrivals.\n\n'+
		'Press Ok to continue using the App!')
	return

def display_data(json_obj):
	# if non-existant stop id used, show pop up and return
    if 'error' in json_obj['resultSet']:
        messagebox.showinfo("", 'No records found for this stop.')
        return

    layout = ''
    for i in json_obj['resultSet']['arrival']:
        stime = datetime.fromtimestamp(int(str(i['scheduled'])) / 1000).strftime('%H:%M:%S')
        layout += str(i['fullSign']) + '\n'
        layout += '\t Scheduled Time: ' + str(stime) + '\n'
        if i['status'] in json_obj == 'estimated':
            time = int(i['estimated']) - int(i['scheduled'])
            if time == 0:
                layout += '\t Status: On Time \n'
            else:
                layout += '\t Status: '  + str(time) + ' behind scheduled \n'
        else:
            layout += '\t Status: On Time \n'
    
    location = ''
    for i in json_obj['resultSet']['location']:
    	location = i['desc']
    	break
    gui = Tk(className = location)
    gui.geometry("450x900")
    gui.resizable(True,True)
    w = Message(gui,text=layout)
    w.pack()
    
def on_submit():
    stop_id = stopId.get()
    minutes = mins.get()
    
	# data validation
    if stop_id.isdigit() == False:
		# put error pop up here and return
        messagebox.showerror("Error", "Stop ID should be in digits!")
        return
    if minutes == '':
        # if not given, default to 20 mins
        minutes = int(20)
    elif minutes.isdigit() == False:
    	# put error pop up here and return
        messagebox.showerror("Error", "Minutes should be in digits!")
        return
    if int(minutes) > 60:
    	# put error pop up here and return
        messagebox.showerror("Error", "Maximum duration is 60 minutes. Default is 20 minutes!")
        return

	# create API URL
    url = base_url + appID + '&locIDs='+ stop_id + '&minutes=' + str(minutes)
    # make get request
    contents = urllib.request.urlopen(url).read()
    
    json_obj = json.loads(contents)
    display_data (json_obj)

# create master view, named as m
m = Tk(screenName=None,  baseName=None,  className='Trimet',  useTk=1)
m.title('Welcome to The Trimet Arrivals App')
m.geometry('300x300')
m.config(bg='blue')


background_image = PhotoImage("trimet.png")
background_label = Label(m, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# create main menu toolbar
menu = Menu(m)
m.config(menu=menu)

#create find station menu 
helpmenu = Menu(menu)
#add it to main menu
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='Visit Trimet Website', command=open_station_browser)
helpmenu.add_command(label='Tutorial', command=open_readme)

#create label for Stop Id, Start time and end time
label1 = Label(m, text="Stop Id", width=5, height=3).grid(row = 1,column = 0)
label2 = Label(m, text="Duration", width=8, height=2).grid(row = 2, column = 0)

# create text fields, in grid format
stopId = Entry(m)
stopId.grid(row = 1,column = 1)
mins = Entry(m)
mins.grid(row = 2,column = 1)



#Creating Submit button
submitButton = Button(m ,text="Submit", width=15, command = on_submit).grid(row=4,column=1)

#Create Quit button
button = Button(m, text='Quit', width=15, command=m.destroy).grid(row = 6,column = 1)

m.mainloop()

