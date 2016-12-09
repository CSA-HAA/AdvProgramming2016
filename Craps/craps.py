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

Rules:
If the come-out roll is 7 or 11, the bet wins.
If the come-out roll is 2, 3 or 12, the bet loses (known as "crapping out").
If the roll is any other value, it establishes a point.
If, with a point established, that point is rolled again before a 7, the bet wins.
If, with a point established, a 7 is rolled before the point is rolled again ("seven out"), the bet loses.

Display:
Information on all the dice and the total
Display the point if no come out
Entry for betting (Between 1 and 1000)
Displays amount bet
Displays balance
#Roll button for rolling and initializing the program

Version .1
Author: Hamzah Ahmed
"""

from tkinter import *
from tkinter import ttk
import random
from tkinter import messagebox

a = [7,11]
def rollDie():
    try:
        if int(balance.get())<=0: #If no balance kicks user out of game also makes sure bet is between 1 and 100
            messagebox.showinfo("Error", "You have run out of money, please come back later.")
            root.destroy()
        if bet.get()=="": #If no bet sets bet
            if int(betting.get())<1:
                bet.set("1")
                betting_entry.delete(0, 'end')
                betting_entry.insert(0, "1")
            elif int(betting.get())>100:
                bet.set("100")
                betting_entry.delete(0, 'end')
                betting_entry.insert(0, "100")
        if bet.get()=="":
            bet.set(betting.get())
        
        global a #rolls 2 dice each going from 1 and 6 and adds them together
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total=dice1+dice2

        #Capital versions are StringVar lowercase varaibles are local variables
        Dice1.set(dice1)
        Dice2.set(dice2)
        Total.set(total)

        if a == [7, 11]: #If not using point yet then gets come out and sets list to total
            round1(total)
            a = []
            a.append(total)
        else: #If come out misses and using point checks if point is recieved 
            if total==a[0] and a!=[7,11]:
                a=[7,11]
                messagebox.showinfo("Victory", "You rolled the winning number!")
                winBet()
                clear()
            elif total==7 and a!=[7,11]:
                a=[7,11]
                messagebox.showinfo("Defeat", "You rolled the losing number!")
                loseBet()
                clear()
    except ValueError: #If words are put in entry for betting tells user their mistake
        messagebox.showinfo("Error", "Please enter a number from 1 and 1000 in numerical format.")
        pass

def round1(total): #First round where come out of 7,11 wins 2,3,12 loses
    if total==7 or total==11 and  a==[7,11]: #a has 7 and 11 in it and total is 7 or 11
        messagebox.showinfo("Victory", "You rolled a winning number!")
        winBet()
        clear()
    elif total==2 or total==3 or total==12  and  a==[7,11]: #List has 7 and 11 and total is 2,3, or 12
        messagebox.showinfo("Defeat", "You rolled a losing number!")
        loseBet()
        clear()
    elif a==[7,11]: #none of the optioons above but list contains 7 or 11
        messagebox.showinfo("Reroll", "You must roll again and get the number you got originally before getting a 7.")
        winnum.set(total)
        
def winBet(): #Adds to balance what was bet and returns the bet as well
    betting_entry.delete(0, 'end')
    balance.set(int(balance.get())+int(bet.get()))
    bet.set("")

def loseBet(): #Takes from balance what was bet
    betting_entry.delete(0, 'end')
    balance.set(int(balance.get())-int(bet.get()))
    bet.set("")

def clear(): #Clear all information on dice and point
    Dice1.set("")
    Dice2.set("")
    Total.set("")
    winnum.set("")

def about(): #Function that opens messagebox and shows version info and program name
    messagebox.showinfo("About", '''If the come-out roll is 7 or 11, the bet wins.\n
If the come-out roll is 2, 3 or 12, the bet loses (known as "crapping out").\n
If the roll is any other value, it establishes a point.\n
If, with a point established, that point is rolled again before a 7, the bet wins.\n
If, with a point established, a 7 is rolled before the point is rolled again ("seven out"), the bet loses.\n
Balance starts at 1000, while betting ranges from 1 and 100.\n
Less then 1 changes betting amount to 1, and greater then 100 changes amount to 100.\n
Upon victory, the bet is taken back, as well as an amount of money equalivalent to the amount bet.\n
Upon defeat, no money is given, and the amount bet is taken away.
\n\nVersion.1\nCreator: Hamzah Ahmed''')

#Sets title and creates gui
root=Tk()
root.title("Craps Game")

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
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=13)
root.grid_rowconfigure(1, weight=13)

#Dice information (individuals and totals as well as the point if used)
Dice1=StringVar()
Dice2=StringVar()
Total=StringVar()
winnum=StringVar()
#Information on what bet is and how much money is owned
bet=StringVar()
balance=StringVar()
betting=StringVar()

#Outcome of first and second dice
ttk.Label(mainframe, textvariable=Dice1).grid(column=1, row=0, sticky=(W, E))
ttk.Label(mainframe, text="Dice 1:").grid(column=0, row=0, sticky=(W, E))

ttk.Label(mainframe, textvariable=Dice2).grid(column=1, row=1, sticky=(W, E))
ttk.Label(mainframe, text="Dice 2:").grid(column=0, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=Total).grid(column=1, row=2, sticky=(W, E)) #Total of 2 dice
ttk.Label(mainframe, text="Total:").grid(column=0, row=2, sticky=(W, E))

ttk.Label(mainframe, textvariable=winnum).grid(column=1, row=3, sticky=(W, E)) #What point needs to be rolled
ttk.Label(mainframe, text="Point:").grid(column=0, row=3, sticky=(W))

ttk.Label(mainframe, textvariable=bet).grid(column=4, row=2, sticky=(E)) #How much money is being bet
ttk.Label(mainframe, text="Bet:").grid(column=3, row=2, sticky=(E))

ttk.Label(mainframe, textvariable=balance).grid(column=4, row=3, sticky=(E)) #States how much money is on hand
ttk.Label(mainframe, text="Balance:").grid(column=3, row=3, sticky=(E))

if balance.get()=="": #If no established balance (beginning of game) sets it to 1000
    balance.set("1000")

#Spot for entering what will be bet
betting_entry = ttk.Entry(mainframe, width=7, textvariable=betting)
betting_entry.grid(column=4, row=0, sticky=(W, E))
ttk.Label(mainframe, text="Lowest Bet: 1").grid(column=3, row=0, sticky=(E))
ttk.Label(mainframe, text="Highest: 100").grid(column=3, row=1, sticky=(E))


rollbttn= ttk.Button(mainframe, text="Roll", command=rollDie)
rollbttn.grid(column=1, row=4, sticky=(E))

#sets window size
root.minsize(width=300, height=180)
root.maxsize(width=300, height=180)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()
