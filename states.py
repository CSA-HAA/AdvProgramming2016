"""
 States Assignment
 Teacher: Mr. Davis
 Created by: Hamzah Ahmed
 Advanced Programming
 Date: September 19th, 2016
 Version 1.0
 Program Description: 
 Creates an Entry Box for the users name
 Creates a ComboBox with 5 states
 When the person chooses ComboBox prints a nice statement to greet them
"""

#Import tkinter to make gui
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Sets title and creates gui
root = Tk()
root.title("States")

#Configures column and row settings and sets padding
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

def greet(*args): #Gets name and choice and displays in a nice greeting
    if namevar.get()=="":
        messagebox.showinfo("Name Error", "Please enter a name")
        state.set("")
    else:
        printer.set("Hi, " + namevar.get().title() + " from " + statevar.get() + "!")

statevar = StringVar()
namevar = StringVar()
printer = StringVar()

#Widgets to put in items, quanitity, and shipping days
name = ttk.Entry(mainframe, width=7, textvariable=namevar)
name.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, text="Name").grid(column=1, row=1, sticky=W)

#Makes combobox
state = ttk.Combobox(mainframe, textvariable=statevar, state='readonly')
state.grid(column=2, row=2, sticky=(W, E))

ttk.Label(mainframe, text="State ").grid(column=1, row=2, sticky=W)

#Gives combobox values
state['values'] = ('Missouri', 'Texas', 'California', 'West Virginia', 'Alaska')
state.bind('<<ComboboxSelected>>', greet)


ttk.Label(mainframe, textvariable=printer).grid(column=2, row=3, sticky=(W))

#Keeps the gui running
root.mainloop()
