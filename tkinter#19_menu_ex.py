from tkinter import*
import tkinter

win=Tk()

x=Menubutton(win,text="courses",relief=RAISED)
x.grid()
x.menu=Menu(x,tearoff=0)
x["menu"]=x.menu

pythonVar=IntVar()
javaVar=IntVar()
phpVar=IntVar()

x.menu.add_checkbutton(label="python",variable=pythonVar)
x.menu.add_checkbutton(label="java",variable=javaVar)
x.menu.add_checkbutton(label="php",variable=phpVar)

x.pack()
win.mainloop()

