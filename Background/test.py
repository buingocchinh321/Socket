import tkinter
import time

from tkinter import *

def window():
    global log_screen
    log_screen = Tk()
    log_screen.title("Client")
    log_screen.geometry('500x500')
    log_screen.configure(bg="pink")


def Login_Screen():
    global lbl 
    global btn
    global space
    space = Label(log_screen, text="", background='pink')
    space.pack()
    lbl = Label(log_screen, text="Username", background='pink')
    lbl.pack()
    #lbl.grid(column=0, row=0)   
    btn = Button(log_screen, text="Login", width=5, height=0, bg="skyblue", fg="black", command=Login)
    btn.pack()
    #btn.grid(column=0, row=1)
    #Login_Screen()
    #lbl.destroy()

def Login():
    btn.destroy()
    lbl.destroy()

window()
Login_Screen()
log_screen.mainloop()

#log_screen.mainloop()