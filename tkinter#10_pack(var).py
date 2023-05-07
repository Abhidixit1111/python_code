import tkinter
from tkinter import*

win=Tk()
win.geometry("400x400")
var=StringVar()
label=Label(win,textvariable=var,relief=RAISED,bg='red')
var.set("hello abhishek dixit")
label.pack()
win.mainloop()
