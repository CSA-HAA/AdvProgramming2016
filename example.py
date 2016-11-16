"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>

This is an example program t show how message box is created
Version .1
Author: Hamzah Ahmed
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def about(): #Function that opens messagebox and shows version info and program name
    messagebox.showinfo("Version", "Login Program\nVersion .1") 

def save(): #Writes all user inputs into file
    
    with open("login.csv", "a") as file:
        file.write(name.get().title() + "," + str(onevar.get()) + "," + str(twovar.get()) + "," + str(threevar.get())) #Get name from StringVar?

        file.write("\n")
        
    messagebox.showinfo("Information Saved", "Your information has been saved to a file!")
    #Reseting GUI
    clearAll()

def clearAll(): #Makes the gui clear of all data
    name_entry.delete(0, END)
    onevar.set(False)
    twovar.set(False)
    threevar.set(False)


#Sets title and creates gui
root=Tk()
root.title("Login")

#Creates menu which options will be added
topMenu=Menu(root)
root.config(menu=topMenu)

#Creates menu and submenus
subMenu=Menu(topMenu)

#Gives menu File option and exit as a suboption which exits program
topMenu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Exit", command=root.destroy)

#Gives menu help option and About as a suboption
helpMenu=Menu(topMenu)
topMenu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About", command=about)

#Makes grid and places it
content = ttk.Frame(root, padding=(3,3,12,12))
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100) #Gives it a sunken border makes it more obvious
namelbl = ttk.Label(content, text="Name")

name = StringVar()
name_entry = ttk.Entry(content, textvariable=name) #Entry to put name

#Variables which checkbuttons attached to
onevar = BooleanVar()
twovar = BooleanVar()
threevar = BooleanVar()

#Predefining which buttons are selected
onevar.set(True)
twovar.set(False)
threevar.set(True)

#Giving buttons text and assigning
one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)

#Buttons that are directed to each command that do an action based on commands function
ok = ttk.Button(content, text="Okay", command=save)
cancel = ttk.Button(content, text="Cancel", command=clearAll)


#Placing everything onto the GUI in a spot
content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
name_entry.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)

#Gives everything a weight as to show when it will grow (Some grow faster)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

root.mainloop()
