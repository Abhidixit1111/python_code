import tkinter as tk
win=tk.Tk()
win.geometry("400x300")
frame1=tk.Frame(master=win,width=100,height=100,bg='orange')
frame1.pack(fill=tk.BOTH,side=tk.TOP,expand=True)
frame2=tk.Frame(master=win,height=100,width=100,bg='white')
frame2.pack(fill=tk.BOTH,side=tk.TOP,expand=True)

frame3=tk.Frame(master=win,height=100,width=100,bg='green')
frame3.pack(fill=tk.BOTH,side=tk.TOP,expand=True)
