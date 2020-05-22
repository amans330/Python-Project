from tkinter import *
from tkinter import ttk
import webbrowser
find_stations_url = 'https://trimet.org/ride/stop_select_form.html'

def open_station_browser():
	''' Opens the web page to find station id for any location
		The API for finding station id from address is not available
		and not exposed by trimet. The user will use this station id to search for arrivals data
	'''
	webbrowser.open_new(find_stations_url)


# create master view
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

stopId = Entry(m).grid(row = 1,column = 1)
start = Entry(m).grid(row = 2,column = 1)
end = Entry(m).grid(row = 3,column = 1)

def clicked():
    res = "Details for " + str(stopId) + " are"
    
#Creating Submit button
submitButton = Button(m ,text="Submit", command = clicked).grid(row=4,column=1,sticky='NS')
# submitButton.bind()
#Creating Quit button
button = Button(m, text='Quit', width=15, command=m.destroy).grid(row = 5,column = 1,sticky='NS')
m.mainloop()

