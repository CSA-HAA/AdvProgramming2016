"""
 Multiple Item Order Form Assignment
 Teacher: Mr. Davis
 Created by: Hamzah Ahmed
 Advanced Programming
 Date: September 7th, 2016
 Version 1.0
 Program Description: 
 Makes a GUI in which you enter shipping and the item you're purchasing.
 Calculates purchase with shipping as well as tax and returns total and tax
 You can have multiple quantities of one item and purchase up to 4 items
"""

#Import tkinter to make gui
from tkinter import *
from tkinter import ttk

#Calculates the total from all times and quanities and shipping price
def calculate(*args):
    file = open("items.txt", "r")
    lines = [i.strip('\n') for i in file]
    try:
        x = []
        x2 = []
        x3 = []
        x4 = []
        y = []
        untaxed = None
        value = item.get().lower().capitalize()
        value2 = item2.get().lower().capitalize()
        value3 = item3.get().lower().capitalize()
        value4 = item4.get().lower().capitalize()
        num = number.get()
        num2 = number2.get()
        num3 = number3.get()
        num4 = number4.get()
        days = shipping.get()
        if days == "2":
            days = 25
        elif days == "3":
            days = 10
        elif days == "5":
            days = 5
        else:
            days = None

        y = days

        if num == '':
            num = 1
        if num2 == '':
            num2 = 1
        if num3 == '':
            num3 = 1
        if num4 == '':
            num4 = 1
        try:
            for i in lines:
                compare = i.split(" - ")
                if compare[:-1][0].lower().capitalize() == value:
                    x = (int(compare[-1]))
                elif compare[:-1][0].lower().capitalize() == value2:
                    x2 = (int(compare[-1]))
                elif compare[:-1][0].lower().capitalize() == value3:
                    x3 = (int(compare[-1]))
                elif compare[:-1][0].lower().capitalize() == value4:
                    x4 = (int(compare[-1]))
        except TypeError:
            pass
        
        if value == '':
            x = 0
        if value2 == '':
            x2 = 0
        if value3 == '':
            x3 = 0
        if value4 == '':
            x4 = 0
            
        untaxed = (x * int(num)) + (x2 * int(num2)) + (x3 * int(num3)) + (x4 * int(num4))
        thetax = untaxed*.0825
        tax.set(format(thetax, '.2f'))
        t = y + (untaxed + thetax)
        total.set(format(t, '.2f'))
        file.close()
    except ValueError:
        pass
    except IndexError:
        pass
    except TypeError:
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
item2 = StringVar()
item3 = StringVar()
item4 = StringVar()
number = StringVar()
number2 = StringVar()
number3 = StringVar()
number4 = StringVar()
shipping = StringVar()
total = StringVar()
tax = StringVar()

#Widgets to put in items, quanitity, and shipping days
item_entry = ttk.Entry(mainframe, width=7, textvariable=item)
item_entry.grid(column=2, row=2, sticky=(W, E))

item_entry2 = ttk.Entry(mainframe, width=7, textvariable=item2)
item_entry2.grid(column=2, row=3, sticky=(W, E))

item_entry3 = ttk.Entry(mainframe, width=7, textvariable=item3)
item_entry3.grid(column=2, row=4, sticky=(W, E))

item_entry4 = ttk.Entry(mainframe, width=7, textvariable=item4)
item_entry4.grid(column=2, row=5, sticky=(W, E))

number_entry = ttk.Entry(mainframe, width=7, textvariable=number)
number_entry.grid(column=1, row=2, sticky=(W, E))

number_entry2 = ttk.Entry(mainframe, width=7, textvariable=number2)
number_entry2.grid(column=1, row=3, sticky=(W, E))

number_entry3 = ttk.Entry(mainframe, width=7, textvariable=number3)
number_entry3.grid(column=1, row=4, sticky=(W, E))

number_entry4 = ttk.Entry(mainframe, width=7, textvariable=number4)
number_entry4.grid(column=1, row=5, sticky=(W, E))

shipping_entry = ttk.Entry(mainframe, width=7, textvariable=shipping)
shipping_entry.grid(column=2, row=6, sticky=(W, E))

#Makes a spot to put in total price and tax
ttk.Label(mainframe, textvariable=tax).grid(column=3, row=7, sticky=(E))
ttk.Label(mainframe, textvariable=total).grid(column=3, row=8, sticky=(E))

#Adds a calculate button
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=9, sticky=W)

#Adds labels to give information on what entering and what total and tax are
ttk.Label(mainframe, text="Item").grid(column=2, row=1, sticky=W)
ttk.Label(mainframe, text="Number").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Shipping Days").grid(column=3, row=6, sticky=W)
ttk.Label(mainframe, text="tax").grid(column=3, row=7, sticky=W)
ttk.Label(mainframe, text="total").grid(column=3, row=8, sticky=W)

#Adds padding
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

#Opens up with item selected and allows you to enter item without having to click it
item_entry.focus()
#Runs calculate if click enter
root.bind('<Return>', calculate)

#Keeps the gui running
root.mainloop()
