"""
 DataBase Assignment
 Teacher: Mr. Davis
 Created by: Hamzah Ahmed
 Advanced Programming
 Date: September 22nd, 2016
 Version 1.0
 Program Description:
 Creates a database with:
 First name entry
 Last name entry
 Radio button with 'business' 'residence' 'other' as options
 State ComboBox
 Yes/No check box for "Accept User Policy"
 Submit button that then writes all of the above into a csv file
"""

#Import tkinter to make gui
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Sets title and creates gui
root = Tk()
root.title("Entry Form")

#After sumbitting with no selected and then switching to yes afterwards as long as a radiobutton is seletected, data is saved?
def submit(*args): #Realign?
    file = open("data.csv", "a")
    # Check required fields
    if first.get() and last.get() and option.get() and state.get():
        # Check Constraints before saving
        if yes.get() == '1':
            file.write(last.get().title() + "," + first.get().title() + "," + option.get() + "," + state.get() + '\n')
            printer.set("Data Saved!")
        else:
            messagebox.showinfo("Unauthorized", "You must accept terms to continue.")
    else:
        messagebox.showinfo("Incomplete Information", "Please fill out all parts of the form")
        
#Configures column and row settings and sets padding
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

first = StringVar()
last = StringVar()
option = StringVar()
statevar = StringVar()
printer = StringVar()
yes = StringVar()

#Widgets to put in name
firstvar = ttk.Entry(mainframe, width=15, textvariable=first)
firstvar.grid(column=2, row=1, sticky=(N, W))

lastvar = ttk.Entry(mainframe, width=15, textvariable=last)
lastvar.grid(column=2, row=2, sticky=(N, W))

ttk.Label(mainframe, text="First Name").grid(column=1, row=1, sticky=(W))
ttk.Label(mainframe, text="Last Name").grid(column=1, row=2, sticky=(W))

business = ttk.Radiobutton(mainframe, text='Business', variable=option, value='Business')
residence = ttk.Radiobutton(mainframe, text='Residence', variable=option, value='Residence')
other = ttk.Radiobutton(mainframe, text='Other', variable=option, value='Other')

business.grid(column=1, row=3, sticky=(W, E))
residence.grid(column=2, row=3, sticky=(W, E))
other.grid(column=3, row=3, sticky=(W, E))

state = ttk.Combobox(mainframe, textvariable=statevar, state='readonly')
state.grid(column=2, row=4, sticky=(W))

ttk.Label(mainframe, text="State").grid(column=1, row=4, sticky=W)
state['values'] = ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachussetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvannia', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming')

#Creates yes checkbutton
yesvar = ttk.Checkbutton(mainframe, text='Yes', variable=yes)
yesvar.grid(column=2, row=5, sticky=(W, E))

ttk.Label(mainframe, text="Accept Policy").grid(column=1, row=5, sticky=(W))

#Adds a calculate button
ttk.Button(mainframe, text="Submit", command=submit).grid(column=3, row=9, sticky=W)

ttk.Label(mainframe, textvariable=printer).grid(column=2, row=9, sticky=(E))

root.bind('<Return>', submit)

#Keeps the gui running
root.mainloop()
