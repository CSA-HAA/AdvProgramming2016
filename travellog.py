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

Creates a list box, text box, and progress bar. As program continues progress bar is updated and the submiting leads it to 100%
Clearing clears everything and reutrns everything to default state
Version .1
Author: Hamzah Ahmed
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Sets message when aboout is clicked in menu
def about(): #Function that opens messagebox and shows version info and program name
    messagebox.showinfo("About", "Click the country you have visited and enter a description of the experience you had. Submit when you are done to have the information recorded.\nThe progress of the user is tracked as they go through the program.\nThe purpose of the program is to keep a record of the users experience in differnet countries.")

def progress(*args): #progressbar is set to be 50% completed
    progressvar.set(50)

def submitted(*args): #Progressbar is set to be fully completed and states information recorded

    if t.get("1.0", END)=="\n":
        messagebox.showinfo("Error", "No information entered in description.")
    else:
        progressvar.set(100)
        messagebox.showinfo("Information Submitted", "Your information has been recorded.")

def clear(*args): #Clears everything and returns gui to start of program
    l.selection_clear(0, END)
    t.delete('1.0', END)
    progressvar.set(0)
    
#Sets title and creates gui
root=Tk()
root.title("Travel log")

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

#Configures column and row settings and sets padding
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#Creates list of countries alphabetically
countries=["Finland", "France", "Greece", "Iceland", "Greenland","Russia", "Brazil", "Spain", "China", "Japan", "United States", "North Korea", "Soth Korea", "Italy", "Barbados", "Belarus", "Belgium", "United Kingdom"]
countries.sort()

#Creates listbox
l=Listbox(mainframe, height=5)
l.grid(column=0, row=0, sticky=(N,W,E,S))

#Adds items in list to listbox
for i in countries:
    l.insert('end', i)

#Creates scrollbar and attaches to list box
s=ttk.Scrollbar(mainframe, orient=VERTICAL, command=l.yview)
s.grid(column=1, row=0, sticky=(N,S))
l['yscrollcommand'] = s.set

#Grows the items in the gui
ttk.Sizegrip().grid(column=1, row=1, sticky=(S,E))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)

#Creates text widget
t = Text(mainframe, width=20, height=10)
t.grid(column=0,row=1)

#Creates progessbar widget
progressvar=IntVar()

p=ttk.Progressbar(mainframe, variable=progressvar,orient=VERTICAL, length=200, mode='determinate')
p.grid(column=2, row=0, sticky=(N,S))

#Activates progress function if something in listbox is selected
l.bind('<<ListboxSelect>>', progress)

#Submitting calls submitted function to set progressbar to 100 and statemessage box has been completed
subbttn= ttk.Button(mainframe, text="Submit", command=submitted)
subbttn.grid(column=1, row=1, sticky=(S, W, E))

#Clears all inputs and returns program to how it was in the beginning
clearbttn= ttk.Button(mainframe, text="Clear", command=clear)
clearbttn.grid(column=1, row=1, sticky=(N, W, E))

#sets minsize
root.minsize(width=400, height=400)
#Gives padding to widgets
for child in mainframe.winfo_children(): child.grid_configure(padx=10, pady=10)


#Runs loop for gui
root.mainloop()

