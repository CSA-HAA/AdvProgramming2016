"""
 Create Login Assignment
 Teacher: Mr. Davis
 Created by: Hamzah Ahmed
 Advanced Programming
 Date: September 12th, 2016
 Version 1.0
 Program Description: 
 A frame with username entry, and password entry
 A button with the text Login, and a label with a result text (successful/access denied). 
The login command will check the attached txt file for the username and password combination. The file is written in ROT13 cypher.
"""

#Import tkinter to make gui
from tkinter import *
from tkinter import ttk
import codecs

#Program that results when user attempts to log in
def login(*args):
    file = open("rot13.txt", "r")
    lines = file.readlines()
    uname = user.get()
    pword = pw.get()

    for i in lines:
        x = i.split()
        if codecs.encode(uname,'rot13') == x[0] and codecs.encode(pword,'rot13') == x[1]:
            result.set("Successful")
            break;
        else:
            result.set("Access Denied")
            
root = Tk()
root.title("Login")

#Configures column and row settings and sets padding
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe['borderwidth'] = 5
mainframe['relief'] = "solid"
mainframe.grid(column=1, row=1, columnspan=3, rowspan=2)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

mainframe2 = ttk.Frame(root, width=130, height=70, padding="3 3 12 12")
mainframe2.grid_propagate(False)
mainframe2['borderwidth'] = 5
mainframe2['relief'] = "solid"
mainframe2.grid(column=1, row=3, columnspan=1, rowspan=3)
mainframe2.columnconfigure(0, weight=1)
mainframe2.rowconfigure(0, weight=1)

mainframe3 = ttk.Frame(root, padding="3 3 12 12")
mainframe3['borderwidth'] = 5
mainframe3['relief'] = "solid"
mainframe3.grid(column=2, row=5)
mainframe3.columnconfigure(0, weight=1)
mainframe3.rowconfigure(0, weight=1)

#anchors for widgets
user = StringVar()
pw = StringVar()
result = StringVar()

#Asks user input
user_entry = ttk.Entry(mainframe, width=20, textvariable=user)
user_entry.grid(column=2, row=1, sticky=(W, E))

pw_entry = ttk.Entry(mainframe, width=20, textvariable=pw)
pw_entry.grid(column=2, row=2, sticky=(W, E))


#Labels to make user-friendly and able to understand
ttk.Label(mainframe, text="Username ", width=13).grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Password ", width=13).grid(column=1, row=2, sticky=W)
ttk.Label(mainframe2, text="").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe2, text="Result").grid(column=1, row=4, sticky=W)
ttk.Label(mainframe2, text="Picture").grid(column=1, row=5, sticky=W)

#Button to log in
ttk.Button(mainframe3, text="Login", command=login).grid(column=3, row=5, sticky=(W,E))

#Makes a spot to put in result
ttk.Label(mainframe2, textvariable=result, width=11).grid(column=2, row=4, sticky=(E))
#Opens up with item selected and allows you to enter username without having to click it
user_entry.focus()
#Runs calculate if click enter
root.bind('<Return>', login)
root.mainloop()
