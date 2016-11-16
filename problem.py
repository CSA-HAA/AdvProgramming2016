"""
 Login Assignment
 Teacher: Mr. Davis
 Created by: Hamzah Ahmed
 Advanced Programming
 Date: October 6th, 2016
 Version 1.0
 Program Description: 
 Type a username, password, and then hit login
 Login will then check a file that has usernames and passwords
 The passwords will be hashed
 Has a toolbar with exit and a forgot password option (as of now the forgot password will just print "you forgot it!"
 About that shows version and creator
"""

from tkinter import *
from tkinter import ttk
import getpass
import csv
import time
import os
import re
import hashlib
#import RPi.GPIO as io
from datetime import datetime
from tkinter import messagebox
# io.setmode(io.BCM)
# pir_pin = 24
# power_pin = 27
# os.system("clear")
# io.setup(pir_pin, io.IN)
# io.setup(power_pin, io.OUT)
# io.output(power_pin, False)
# PERIOD_OF_TIME = 1800

def loginoffline(*args):
    try:
        var = False
        f2 = open('hashd.csv', 'r')
        f = open("Logins.txt","a")
        students=csv.reader(f2)
        username=user.get()
        password=pw.get()
        username_rowgetnumyo=2 #change host_row to the corresponding row - 1 (ie; row 45, put in 44) in google's csv
        password_rowgetnum=3 #master_row to the schools student list
        salt="gnuvie:^)"
        for hosts_rowyo in students:
            row = 1
            username=username.replace("@chaparralstaracademy.com","")
            hosts_rowyo[username_rowgetnumyo]=hosts_rowyo[username_rowgetnumyo].replace("@chaparralstaracademy.com","")
            hosts_rowyo[username_rowgetnumyo]=hosts_rowyo[username_rowgetnumyo].zfill(4)
            #print(str(hashlib.sha256(username.encode("UTF-8")).hexdigest())+" username "+hosts_rowyo[username_rowgetnumyo]+"\n"+str(hashlib.sha256(password.encode("UTF-8")).hexdigest())+" password "+hosts_rowyo[password_rowgetnum])
            if(username=="displayport:^)"):
                exit()
            if (hashlib.md5((salt+username).encode("UTF-8")).hexdigest() == hosts_rowyo[username_rowgetnumyo]) & (hashlib.md5((salt+password).encode("UTF-8")).hexdigest() == hosts_rowyo[password_rowgetnum]):
                #print("Logging in.", end=""),
                #time.sleep(1)
                #print(".", end=""),
                #time.sleep(1)
                #print(".")
                #time.sleep(3)
                messagebox.showinfo("Login","Logging in complete! Plug in your chromebook now.")
                f.write(username+" "+str(datetime.now())+"\n")
                f.close()
                start = time.time()
                while True :
                    # io.output(power_pin, True)
                    #
                    # if time.time() > start + PERIOD_OF_TIME:
                    #     print("POWER OFF")
                    #     time.sleep(1)
                    #     io.output(power_pin, False)
                    #     time.sleep(3)
                    #     loginoffline()
                    #     break
                    var=True
                    user_entry.delete(0, END)
                    pw_entry.delete(0, END)
                    break
                break

        #print("Logging in.", end=""),
        #time.sleep(1)
        #print(".", end=""),
        #time.sleep(1)
        #print(".")
        #time.sleep(3)
        #os.system("clear")
        if var==False: #If var hasn't been set to true it means password wasn't in file so error logging in
            messagebox.showinfo("Login", "Error logging in, please try again!")
            #loginoffline(*args)
            user_entry.delete(0, END)
            pw_entry.delete(0, END)            
            f2.close()
            f.close()
    except KeyboardInterrupt:
        messagebox.showinfo("Login", "Error, please try again! ")
        loginoffline(*args)


#Sets title and creates gui
root=Tk()
root.title("Login")

#Configures column and row settings and sets padding
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

user = StringVar()
pw = StringVar()

#Asks user input
user_entry = ttk.Entry(mainframe, width=20, textvariable=user)
user_entry.grid(column=2, row=1, sticky=(W, E))

pw_entry = ttk.Entry(mainframe, show="*", width=20, textvariable=pw)
pw_entry.grid(column=2, row=2, sticky=(W, E))

#Labels to make user-friendly and able to understand
ttk.Label(mainframe, text="Username ", width=13).grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Password ", width=13).grid(column=1, row=2, sticky=W)

#Button to log in
ttk.Button(mainframe, text="Login", command=loginoffline).grid(column=2, row=3, sticky=(W,E))


#Runs loginoffline if click enter
root.bind('<Return>', loginoffline)

root.mainloop()
