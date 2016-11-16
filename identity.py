"""
 Name/Age Assignment
 Teacher: Mr. Davis
 Created by: Hamzah Ahmed
 Advanced Programming
 Date: September 16th, 2016
 Version 1.0
 Program Description: 
 Makes a Name Entry widget (with 'name' inserted)
 Makes a Age Entry widget (with 'age' inserted)
 Makes Gender RadioButtons
 Makes a Submit button that clears screen
"""


#Import tkinter to make gui
from tkinter import *
from tkinter import ttk
import time

#Makes the GUI the same way it was at the beginning of the program

def clear():
    try:
        if int(age.get())>=0 and int(age.get())<=200 and (len(name.get())>=2) and gender.get()=='male' or gender.get()=='female' or gender.get()=='other':
            gender.set("0")
            name_entry.delete(0, END)
            age_entry.delete(0, END)
            name_entry.insert(0,'Name')
            age_entry.insert(0, 'Age')
            valid.set("")
        else:
            valid.set("Invalid Entry! Try again.")
            pass
    except TypeError:
        valid.set("Invalid Entry! Try again.")
        pass
    except ValueError:
        valid.set("Invalid Entry! Try again.")
        pass

def callback1(event): #empties name entry widget
    name_entry.delete(0, "end")
    return None

def callback2(event): #empties age entry widget
    age_entry.delete(0, "end")
    return None

#Sets title and creates gui    
root = Tk()
root.title("Identity Form")

#Configures column and row settings and sets padding
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

name=StringVar()
age=StringVar()
gender=StringVar()
valid=StringVar()

#Widgets asking name and age
name_entry = ttk.Entry(mainframe, width=20, textvariable=name)
name_entry.grid(column=1, row=1, sticky=(W, E))

age_entry = ttk.Entry(mainframe, width=20, textvariable=age)
age_entry.grid(column=1, row=2, sticky=(W, E))

#Makes gender radiobuttons all 1 part of gender
male = ttk.Radiobutton(mainframe, text='Male', variable=gender, value='male')
female = ttk.Radiobutton(mainframe, text='Female', variable=gender, value='female')
other = ttk.Radiobutton(mainframe, text='Other', variable=gender, value='other')

male.grid(column=1, row=3, sticky=(E))
female.grid(column=2, row=3, sticky=(E))
other.grid(column=3, row=3, sticky=(W))


#Adds name and age to entries
name_entry.insert(0, 'Name')
age_entry.insert(0, 'Age')

#if entries are clicked goes to callback 1 and 2
name_entry.bind("<Button-1>", callback1)
age_entry.bind("<Button-1>", callback2)

#Makes a button that clears everything and returns it to start of program
ttk.Button(mainframe, text="Submit", command=clear).grid(column=3, row=4, sticky=(E))

ttk.Label(mainframe, textvariable=valid).grid(column=1, row=4, columnspan=2, sticky=(E))

