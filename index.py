from tkinter import *
from tkinter import ttk
import webbrowser
import urllib.request
import json
from tkinter import messagebox

base_url = 'https://developer.trimet.org/ws/v2/arrivals?'
find_stations_url = 'https://trimet.org/ride/stop_select_form.html'
appID = 'appID=294B60BEC29C4DEBD3D8A96AB'

def open_station_browser():
	''' Opens the web page to find station id for any location
		The API for finding station id from address is not available
		and not exposed by trimet. The user will use this station id to search for arrivals data
	'''
	webbrowser.open_new(find_stations_url)

def display_data(json_obj):
    # row = 0
    layout = ''
    for i in json_obj['resultSet']['arrival']:
        print(type(i['fullSign']))
        layout += str(i['fullSign']) + '\t'
        layout += str(i['scheduled']) + '\n'
        # e = Entry(m)
        # e.grid(row=row, column=1, sticky=NSEW)
        # e.insert(END, i['fullSign'])
        # e = Entry(m)
        # e.grid(row=row, column=2, sticky=NSEW)
        # e.insert(END, i['estimated'])
        # row = row+1
    print(layout)
    messagebox.showinfo('Trimet Results', layout)
    
def on_submit():
    stop_id = stopId.get()
    minutes = mins.get()
    
	# data validation
    if stop_id.isdigit() == False:
		# put error pop up here and return
        messagebox.showerror("Error", "Stop ID should be a digit!")
    if minutes == '':
            # if not given, default to 60 mins
        minutes = int(60)
    elif minutes.isdigit() == False:
    	# put error pop up here and return
        messagebox.showerror("Error", "Minutes should in digits!")
        print(False)
	# create API URL
    url = base_url + appID + '&locIDs='+ stop_id + '&minutes=' + str(minutes)
    # make get request
    contents = urllib.request.urlopen(url).read()
    json_obj = json.loads(contents)
    #print(json.dumps(json_obj['resultSet']['arrival'],indent=4))
    display_data (json_obj)

    try:
        int(stop_id)
    except ValueError:
        print (False)

# create master view, named as m
m = Tk(screenName=None,  baseName=None,  className='Trimet',  useTk=1)
m.title('Welcome to The Trimet Arrivals App')

# create main menu toolbar
menu = Menu(m)
m.config(menu=menu)

#create find station menu 
stationmenu = Menu(menu)
#add it to main menu
menu.add_cascade(label='Find Station ID', menu=stationmenu)
stationmenu.add_command(label='stationmenu', command=open_station_browser)

#create label for Stop Id, Start time and end time
label1 = Label(m, text="Stop Id").grid(row = 1,column = 0)
label2 = Label(m, text="From").grid(row = 2, column = 0)
label3 = Label(m ,text = "Until").grid(row = 3,column = 0, sticky='NS')

# create text fields, in grid format
stopId = Entry(m)
stopId.grid(row = 1,column = 1)
mins = Entry(m)
mins.grid(row = 2,column = 1)



#Creating Submit button
submitButton = Button(m ,text="Submit", command = on_submit).grid(row=4,column=1,sticky='NS')
# submitButton.bind()
#Creating Quit button
button = Button(m, text='Quit', width=15, command=m.destroy).grid(row = 5,column = 1,sticky='NS')
m.mainloop()

