import tkinter
from tkinter import*
from tkinter import messagebox

top=Tk()
top.geometry("300x150")
def click():
    messagebox.showinfo("hello","green button  clicked")
a=Button(top,text="yellow",activeforeground="yellow",activebackground="orange",pady=10)
b=Button(top,text="Blue",activeforeground="blue",activebackground="orange",pady=10)
c=Button(top,text="green",command=click,activeforeground="green",activebackground="orange",pady=10)
d=Button(top,text="red",activeforeground="yellow",activebackground="orange",pady=10)

a.pack(side=LEFT)
b.pack(side=LEFT)
c.pack(side=LEFT)
d.pack(side=LEFT)
top.mainloop()
