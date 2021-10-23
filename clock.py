from tkinter import *
from tkinter.ttk import *
from time import strftime
import os 
os.system("cls")
root = Tk()
root.title("clock")
def fetchTime():
    f = strftime("%H : %M : %S : %p")
    label.config(text=f)
    label.after(1000,fetchTime)

label = Label(root,font = ("Algerian",80),background="black",foreground="blue")
label.pack(anchor="center")
fetchTime()
mainloop()