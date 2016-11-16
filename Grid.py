"""
 Grid Assignment
 Teacher: Mr. Davis
 Created by: Hamzah Ahmed
 Advanced Programming
 Date: September 7th, 2016
 Version 1.0
 Program Description: 
Creates a 3x3 login box
Stretches the Login button across columns 2 and 3
Sticks the name label to the top left
Sticks password label to left just below row 1
Text boxes incenter of their columns
Uses padding
Menu has exit from file
Login clears widgets
"""


#Import tkinter to make gui
from tkinter import *
from tkinter import ttk

#Makes the GUI the same way it was at the beginning of the program

def login(*args):
    name_entry.delete(0, END)
    pw_entry.delete(0, END)

#Sets title and creates gui
root=Tk()
root.title("Login")

topMenu=Menu(root)
root.config(menu=topMenu)

#Creates menu and submenus
subMenu=Menu(topMenu)

#Gives menu options
topMenu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Exit", command=root.destroy)

#Configures column and row settings and sets padding
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

name=StringVar()
pw=StringVar()

#Widgets asking name and age
name_entry = ttk.Entry(mainframe, width=20, textvariable=name)
name_entry.grid(column=2, row=1, sticky=(W, E))

pw_entry = ttk.Entry(mainframe, width=20, textvariable=pw)
pw_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Label(mainframe, text="Username").grid(column=1, row=1, sticky=(N, W))
ttk.Label(mainframe, text="Password").grid(column=1, row=2, sticky=(N,W))

ttk.Label(mainframe, text="                      ").grid(column=3, row=3, sticky=(E))

#Makes a button that clears everything and returns it to start of program
ttk.Button(mainframe, text="Login", command=login).grid(column=2, row=3, columnspan=2, sticky=(W, E))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

name_entry.focus()
root.bind('<Return>', login)

root.mainloop()
