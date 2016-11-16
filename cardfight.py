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

This is a fighting program where a card is picked on right and left side and they fight each other
Wins and losses are counted
Version .1
Author: Hamzah Ahmed
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Character:
    def __init__(self, name, attack, defense, health):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.health = health
        self.total = attack+defense+health

#Left side characters
Rash = Character("Rash", 42, 50, 80)
Untss = Character("Untss", 15, 54, 100)
Ilora = Character("Ilora", 60, 35, 80)
                                    #Both sides have totals of 165 168 and 175
#Right side characters
Zys = Character("Zys", 12, 97, 83)
Eentha = Character("Eentha", 55, 17, 90)
Dant = Character("Dant", 73, 28, 88)

left_characters = {        
    "Rash": Character("Rash", 42, 50, 80),
    "Untss": Character("Untss", 15, 54, 100),
    "Ilora": Character("Ilora", 60, 35, 80),
}

right_characters = {
    "Zys": Character("Zys", 12, 97, 83),
    "Eentha": Character("Eentha", 55, 17, 90),
    "Dant": Character("Dant", 73, 28, 88),
}

leftnames = list(left_characters.keys())
rightnames = list(right_characters.keys())

def about(): #Function that opens messagebox and shows version info and program name
    messagebox.showinfo("Version", "Card Fight\nVersion .1")

def statDisplay1(*args): #Displays stats for characters in left box
    idxs = lbox.curselection()[0]
    saveattack = 0
    savedefense = 0
    
    savehealth = 0
    savename=""
    if idxs == 0:
        savename="Rash"
        saveattack = Rash.attack
        savedefense = Rash.defense
        savehealth = Rash.health
    elif idxs==1:
        savename="Untss"
        saveattack = Untss.attack
        savedefense = Untss.defense
        savehealth = Untss.health
    elif idxs==2:
        savename="Ilora"
        saveattack = Ilora.attack
        savedefense = Ilora.defense
        savehealth = Ilora.health
    statusmsg1.set(savename+"\nAttack: "+str(saveattack)+"\nDefense: "+str(savedefense)+"\nHealth: "+str(savehealth))

def statDisplay2(*args): #Displays stats for characters in right box
    idxs = rbox.curselection()[0]
    saveattack = 0
    savedefense = 0
    savehealth = 0
    savename=""
    if idxs == 0:
        savename="Zys"
        saveattack = Zys.attack 
        savedefense = Zys.defense
        savehealth = Zys.health
    elif idxs==1:
        savename="Eentha"
        saveattack = Eentha.attack
        savedefense = Eentha.defense
        savehealth = Eentha.health
    elif idxs==2:
        savename="Dant"
        saveattack = Dant.attack
        savedefense = Dant.defense
        savehealth = Dant.health
    statusmsg2.set(savename+"\nAttack: "+str(saveattack)+"\nDefense: "+str(savedefense)+"\nHealth: "+str(savehealth))


def fight(): #Part of code that checks for wins and loss checks which has greater total stats and deletes from list box

    try:
        namel = lbox.get(lbox.curselection()[0])
        namer = rbox.get(rbox.curselection()[0])
        
        totalleft = left_characters[namel].total
        totalright = right_characters[namer].total

        lbox.delete(lbox.curselection()[0])
        rbox.delete(rbox.curselection()[0])

        if totalleft > totalright : #Checks if won or lost
            wins.set(wins.get()+"\n"+namel)
            loss.set(loss.get()+"\n"+namer)
        else:
            wins.set(wins.get()+"\n"+namer)
            loss.set(loss.get()+"\n"+namel)
    except IndexError:
            pass
    
#Sets title and creates gui
root=Tk()
root.title("Card Fight")

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
mainframe = ttk.Frame(root, padding=(5, 5, 12, 0))
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

#Makes a listbox on left side
leftnames = ('Rash', 'Untss', 'Ilora')
lnames = StringVar(value=leftnames)
lbox = Listbox(mainframe, listvariable=lnames, exportselection=0, height=3)
lbox.grid(column=0, row=0)

statusmsg1= StringVar()
status1 = ttk.Label(mainframe, textvariable=statusmsg1)
status1.grid(column=0, row=1, rowspan=3, sticky=W)

#Makes listbox for characters on right side
rightnames = ('Zys', 'Eentha', 'Dant')
rnames = StringVar(value=rightnames)
rbox = Listbox(mainframe, listvariable=rnames, exportselection=0, height=3)
rbox.grid(column=1, row=0)
#Disables right listbox for random use instead of user

statusmsg2= StringVar()
status2 = ttk.Label(mainframe, textvariable=statusmsg2)
status2.grid(column=1, row=1, rowspan=3, sticky=W)

#Shows users wins and lossses

wins = StringVar()
loss = StringVar()
#Labels the wins and losses
ttk.Label(mainframe, text="Wins", width=13).grid(column=2, row=0, sticky=N)
ttk.Label(mainframe, text="Loss", width=13).grid(column=2, row=1, sticky=N)
#Adds the character that won their match and the ones that lost their match
ttk.Label(mainframe, textvariable=wins).grid(column=2, row=0, sticky=(S,E))
ttk.Label(mainframe, textvariable=loss).grid(column=2, row=1, sticky=(S, E))

#Shows stats of character when clicked
lbox.bind('<<ListboxSelect>>', statDisplay1)
rbox.bind('<<ListboxSelect>>', statDisplay2)

#Button for fighting
fightbttn= ttk.Button(mainframe, text="Fight", command=fight)
fightbttn.grid(column=3, row=3, sticky=(E))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()
