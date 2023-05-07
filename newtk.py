from tkinter import*
import tkinter as tk
win=tk.Tk()
win.geometry("400x400")
w=Label(win,text="hello i am abhishek")
frame1=tk.Frame(master=win,height="400",width="400",bg="red")
frame1.pack()
w.pack()
win.mainloop()
