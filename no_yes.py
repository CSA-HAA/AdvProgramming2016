"""
 no_yes Form Assignment
 Teacher: Mr. Davis
 Created by: Hamzah Ahmed
 Advanced Programming
 Date: September 14th, 2016
 Version 1.0
 Program Description:
 Create a form that has a no/yes checkbutton, a button that says hi (that is disabled), and a label that has nothing in it
 When the person checks yes, the Hi button is enabled
 When the check no, the Hi button is disabled
 When the user clicks Hi (after it is enabled of course) the label goes to "Hi!
 """

#Import tkinter to make gui
from tkinter import *
from tkinter import ttk

#Disables hi button if no is enabled and unchecks yes
def changed(*args):
    if b1.get()=="1":
        button.state(['disabled'])
        result.set("")
        b2.set('0')

#Enabless hi button if yes is enabled and unchecks no
def changed2():
    if b2.get() == "1":
        button.state(['!disabled'])
        b1.set('0')
    else:
        result.set("")
    
#Makes label say hi        
def printHi():
    result.set('Hi!')
    
#Sets title and creates gui
root = Tk()
root.title("Form")

#Configures column and row settings and sets padding
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#Creates no checkbutton
b1 = StringVar()
c1 = ttk.Checkbutton(mainframe, text='No', 
	    command=changed, variable=b1)
c1.grid(column=1, row=2, sticky=(W, E))

#Creates yes check button
b2 = StringVar()
c2 = ttk.Checkbutton(mainframe, text='Yes', 
	    command=changed2, variable=b2)
c2.grid(column=1, row=1, sticky=(W, E))

#Creates disabled hi button that if clicked sets label on the side of hi
button = ttk.Button(mainframe, text="Hi", command=printHi, state='disabled')
button.grid(column=2, row=3, sticky=W)

#Label that says hi if Hi! button is clicked
result = StringVar()
ttk.Label(mainframe, textvariable=result).grid(column=1, row=3, sticky=(W))

