import tkinter as tk
from tkinter import*
from tkinter import messagebox

top=Tk()
top.geometry("400x400")
def click():
    messagebox.showinfo()

for i in range(1,5):
    for j in range(1,4):
        frame=tk.Frame(master=top,relief=tk.RAISED,borderwidth=2)
        frame.grid(row=i,column=j,padx=5,pady=5)
        a=Button(top,text="yellow",activeforeground="yellow",activebackground="orange",pady=10)
        a.pack()
top.mainloop()

