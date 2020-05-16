from tkinter import *
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

# create main menu toolbar
menu = Menu(m)
m.config(menu=menu)
#create find station menu 
stationmenu = Menu(menu)
#add it to main menu
menu.add_cascade(label='Find Station ID', menu=stationmenu)
stationmenu.add_command(label='stationmenu', command=open_station_browser)

# create label
heading=Label(m, text='Welcome to The Trimet Arrivals Information App')
heading.pack()

# create button
button = Button(m, text='Quit', width=25, command=m.destroy) 
button.pack() 
m.mainloop()

