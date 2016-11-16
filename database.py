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

Makes following:
-Enter for PO
-Entry for a customer name
-Entry for customer (street address, city, state)
-Entry for what all they purchased (this needs to be more than one line, a descriptive box)
-Entry for purchase date
-Entries for item price, tax (8.25 percent), shipping, and then print the total cost
Writes to a file and also reterieves information based on PO
Version .2
Author: Hamzah Ahmed
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def about(): #Function that opens messagebox and shows version info and program name
    messagebox.showinfo("About", "Fill out the form and click submit when you are done.\nClick retrieve if you want to pull out a form you have already stored.\nThis database records user information for storing a record of for any purposes in the future.\nVersion.2\nCreator: Hamzah Ahmed")

def setRange(*args): #Changes spinbox bounds
    if month.get()=="2":
        s1.configure(to=28)
    elif month.get()=="4":
        s1.configure(to=30)
    elif month.get()=="6":
        s1.configure(to=30)
    elif month.get()=="9":
        s1.configure(to=30)
    elif month.get()=="11":
        s1.configure(to=30)

def clearInfo(): #Deletes info inputted by user or preset info from GUI
    first_entry.delete(0, 'end')
    last_entry.delete(0, 'end')
    street_entry.delete(0, 'end')
    street2_entry.delete(0, 'end')
    city_entry.delete(0, 'end')
    zip_entry.delete(0, 'end')
    t.delete('1.0', END)
    price_entry.delete(0, 'end')
    ship_entry.delete(0, 'end')
    s.delete(0, 'end')
    s1.delete(0, 'end')
    tax.set("")
    total.set("")
    state.set('')
    year_combo.set('')

def status(): #Checks to see if a file exists and if a PO is used
    x=False
    try:
        with open("PurchaseOrder.csv", "r") as myfile:
            for i in myfile.readlines():
                if i.split(',')[0]==str(PO.get()):
                    messagebox.showinfo("Error", "The PO is already in use. No changes can be made.")
                    x=True
                    break
        return x
    except FileNotFoundError:
        return x


def submit(*args): #Saves input info into a file and checks to see if the form is completely filled as well as calculates, displays, and saves total price and tax
    try:
        if (len(PO.get())>=1 and len(first.get())>=1 and len(last.get())>=1 and len(street.get())>=1 and len(statevar.get())>=1 and len(city.get())>=1 and len(zipc.get())>=1 and len(t.get("1.0",END).strip('\n'))>=1):
            if len(PO.get())==9 and PO.get().isdigit():
                if len(zipc.get())==5 and zipc.get().isdigit():
                    preround = (float(price.get()) *.0825)
                    taxed = '%.2f' % preround
                    tax.set(taxed)
                    roundprice= '%.2f' % float(price.get())
                    roundship = '%.2f' % float(ship.get())
                    calc= float(taxed) + float(roundprice) + float(roundship)
                    calc='%.2f' %calc
                    total.set(calc)
                    x=status()
                    if x==False:
                        with open("PurchaseOrder.csv", "a") as myfile:
                            myfile.write(PO.get()+','+first.get()+','+last.get()+','+street.get()+','+street2.get()+','+statevar.get()+','+city.get()+','+zipc.get()+','+(t.get("1.0",END)).strip('\n')+','+price.get()+','+str(taxed)+','+month.get()+','+day.get()+','+year.get()+','+ship.get()+','+str(calc)+'\n')
                            messagebox.showinfo("Information Recorded", "Your information has been submitted")
                            PO_entry.delete(0, 'end')
                            clearInfo()
                else:
                    messagebox.showinfo("Error", "Zip code must be 5 digits")

            else:
                messagebox.showinfo("Error", "PO must be 9 digits")
                print(PO.get())
                print(len(PO.get()))
        else:
            messagebox.showinfo("Error", "Invalid Entry")
    except ValueError:
        messagebox.showinfo("Error", "Invalid Entry\nEnter price and shipping in digits.")

def retrieve(*args): #Looks at the PO and retrieves all the information next to PO if PO is there
    clearInfo()
    try:
        if len(PO.get())==9:
            x=None
            with open("PurchaseOrder.csv", "r") as myfile:
                for i in myfile.readlines():
                    if i[0]==PO.get():
                        x=i
                lines=i.split(',')
                idx =lines.index(PO.get())
                first_entry.insert(0,lines[idx+1])
                last_entry.insert(0,lines[idx+2])
                street_entry.insert(0,lines[idx+3])
                street2_entry.insert(0,lines[idx+4])
                statevar.set(lines[idx+5])
                city_entry.insert(0,lines[idx+6])
                zip_entry.insert(0,lines[idx+7])
                t.insert('1.0',lines[idx+8])
                price_entry.insert(0,lines[idx+9])
                tax.set(lines[idx+10])
                s.insert(0,lines[idx+11])
                s1.insert(0,lines[idx+12])
                year.set(lines[idx+13])
                ship_entry.insert(0,lines[idx+14])
                total.set(lines[idx+15].strip('\n'))
        else:
            messagebox.showinfo("Error", "The given PO is not in the database.")
    except ValueError:
        messagebox.showinfo("Error", "The given PO is not in the database.")
    except FileNotFoundError:
        messagebox.showinfo("Error", "No saved entries.")
#Sets title and creates gui
root=Tk()
root.title("Database")

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

#Grows the items in the gui
ttk.Sizegrip().grid(column=1, row=1, sticky=(S,E))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=3)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=3)

#Widgets asking user info PO,name,address
PO=StringVar()
PO_entry = ttk.Entry(mainframe, width=20, textvariable=PO)
PO_entry.grid(column=1, row=0, sticky=(W))
ttk.Label(mainframe, text="PO").grid(column=0, row=0, sticky=(W, E))

first=StringVar()
first_entry = ttk.Entry(mainframe, width=20, textvariable=first)
first_entry.grid(column=1, row=1, sticky=(W))
ttk.Label(mainframe, text="First").grid(column=0, row=1, sticky=(W, E))

last=StringVar()
last_entry = ttk.Entry(mainframe, width=20, textvariable=last)
last_entry.grid(column=1, row=2, sticky=(W))
ttk.Label(mainframe, text="Last").grid(column=0, row=2, sticky=(W, E))

street=StringVar()
street_entry = ttk.Entry(mainframe, width=20, textvariable=street)
street_entry.grid(column=1, row=3, sticky=(W))
ttk.Label(mainframe, text="Street").grid(column=0, row=3, sticky=(W, E))

street2=StringVar()
street2_entry = ttk.Entry(mainframe, width=20, textvariable=street2)
street2_entry.grid(column=1, row=4, sticky=(W))
ttk.Label(mainframe, text="Street(Optional)").grid(column=0, row=4, sticky=(W, E))

#Asks location
statevar = StringVar()
state = ttk.Combobox(mainframe, width=8 ,textvariable=statevar, state='readonly')
state.grid(column=1, row=5, columnspan=4, sticky=(W))
ttk.Label(mainframe, text="State").grid(column=0, row=5, sticky=(W, E))

state['values'] = ("AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY")

city=StringVar()
city_entry = ttk.Entry(mainframe, width=15, textvariable=city)
city_entry.grid(column=2, row=5, sticky=(W))
ttk.Label(mainframe, text="City").grid(column=1, row=5, sticky=(E))

zipc=StringVar()
zip_entry = ttk.Entry(mainframe, width=20, textvariable=zipc)
zip_entry.grid(column=1, row=6, sticky=(W))
ttk.Label(mainframe, text="Zip Code").grid(column=0, row=6, sticky=(W, E))
#Description
t = Text(mainframe, width=18, height=10)
t.grid(column=1, row=7,sticky=(W))
ttk.Label(mainframe, text="Description").grid(column=0, row=7, sticky=(W, E))
#Price date and shipping are asked(gives total and tax)
price=StringVar()
price_entry = ttk.Entry(mainframe, width=10, textvariable=price)
price_entry.grid(column=4, row=0, sticky=(W))
ttk.Label(mainframe, text="Price").grid(column=3, row=0, sticky=(W, E))

tax=StringVar()
ttk.Label(mainframe, textvariable=tax).grid(column=4, row=1, sticky=(W, E))
ttk.Label(mainframe, text="Tax").grid(column=3, row=1, sticky=(W, E))

month = StringVar()
s = Spinbox(mainframe, from_=1, to=12, width=8, textvariable=month, command=setRange)
s.grid(column=4, row=2, sticky=(W))
ttk.Label(mainframe, text="Month").grid(column=3, row=2, sticky=(W, E))

day = StringVar()
s1 = Spinbox(mainframe, from_=1, to=31, width=8, textvariable=day)
s1.grid(column=6, row=2, sticky=(W))
ttk.Label(mainframe, text="Day").grid(column=5, row=2, sticky=(W, E))

year = StringVar()
year_combo = ttk.Combobox(mainframe, width=8 ,textvariable=year, state='readonly')
year_combo['values'] = ('1920','1921','1922','1923','1924','1925','1926','1927','1928','1929',
                        '1930','1931','1932','1933','1934','1935','1936','1937','1938','1939',
                        '1940','1941','1942','1943','1944','1945','1946','1947','1948','1949',
                        '1950','1951','1952','1953','1954','1955','1956','1957','1958','1959',
                        '1960','1961','1962','1963','1964','1965','1966','1967','1968','1969',
                        '1970','1971','1972','1973','1974','1975','1976','1977','1978','1979',
                        '1980','1981','1982','1983','1984','1985','1986','1987','1988','1989',
                        '1990','1991','1992','1993','1994','1995','1996','1997','1998','1999',
                        '2000','2001','2002','2003','2004','2005','2006','2007','2008','2009',
                        '2010','2011','2012','2013','2014', '2015', '2016')
year_combo.grid(column=8, row=2, sticky=(W))
ttk.Label(mainframe, text="Year").grid(column=7, row=2, sticky=(E))

ship = StringVar()
ship_entry = ttk.Entry(mainframe, width=10, textvariable=ship)
ship_entry.grid(column=4, row=3, sticky=(W))
ttk.Label(mainframe, text="Shipping Cost").grid(column=3, row=3, sticky=(W, E))

total=StringVar()
ttk.Label(mainframe, textvariable=total).grid(column=4, row=4, sticky=(W, E))
ttk.Label(mainframe, text="Total").grid(column=3, row=4, sticky=(W, E))

#Submit button when done and retrieve button with given information
subbttn= ttk.Button(mainframe, text="Submit", command=submit)
subbttn.grid(column=7, row=7, sticky=(S, W, E))

retrievebttn= ttk.Button(mainframe, text="Retrieve", command=retrieve)
retrievebttn.grid(column=8, row=7, sticky=(S, W, E))

#sets minsize
root.minsize(width=1000, height=510)
for child in mainframe.winfo_children(): child.grid_configure(padx=10, pady=10)

#Runs loop for gui
root.mainloop()
