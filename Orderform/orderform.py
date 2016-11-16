"""
 Order Form Assignment
 Teacher: Mr. Davis
 Created by: Hamzah Ahmed
 Advanced Programming
 Date: September 6th, 2016
 Version 1.0
 Program Description: 
 Makes a GUI in which you enter shipping and the item you're purchasing.
 Calculates purchase with shipping as well as tax and returns total
"""

#Import tkinter to make gui
from tkinter import *
from tkinter import ttk

#Calculates the total from item price and shipping price
def calculate(*args):
    file = open("items.txt", "r")
    lines = [i.strip('\n') for i in file]
    try:
        x = []
        y = []
        value = item.get()
        days = shipping.get()
        if days == "2":
            days = "Two"
        elif days == "3":
            days = "Three"
        elif days == "5":
            days = "Five"
        else:
            days = None
        for i in lines:
            try:
                if value in i:
                    x = i.split(" - ")
                elif days in i:
                    y = i.split(" - ")
                    y[-1] = y[-1].strip('$')
            except TypeError:
                pass
        t = format(int(y[-1]) + (int(x[-1]) + (int(x[-1])*.0825)), '.2f')
        total.set(t)
        file.close()
    except ValueError:
        pass
    except IndexError:
        pass

#Sets title and creates gui
root = Tk()
root.title("Order Form")

#Configures column and row settings and sets padding
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#Allows for item shipping and total into variables to auto update later if information is changed
item = StringVar()
shipping = StringVar()
total = StringVar()

#Widgets to put in items and shipping days
item_entry = ttk.Entry(mainframe, width=7, textvariable=item)
item_entry.grid(column=2, row=1, sticky=(W, E))
shipping_entry = ttk.Entry(mainframe, width=7, textvariable=shipping)
shipping_entry.grid(column=2, row=2, sticky=(W, E))

#Makes a spot to put in total price
ttk.Label(mainframe, textvariable=total).grid(column=2, row=4, sticky=(E))
#Adds a calculate button
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=5, sticky=W)

#Adds labels to give information on what entering and what tax and total is
ttk.Label(mainframe, text="item").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="shipping days").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="8.25%").grid(column=2, row=3, sticky=E)
ttk.Label(mainframe, text="tax").grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="total").grid(column=3, row=4, sticky=W)

#Adds padding
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

#Opens up with item selected and allows you to enter item without having to click it
item_entry.focus()
#Runs calculate if click enter
root.bind('<Return>', calculate)

#Keeps the gui running
root.mainloop()
