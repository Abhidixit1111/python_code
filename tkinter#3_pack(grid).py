import tkinter as tk
win=tk.Tk()

for i in range(5):
    for j in range(3):
        frame=tk.Frame(master=win,relief=tk.RAISED,borderwidth = 2)
        frame.grid(row=i,column=j)
        label=tk.Label(master=frame,text=f"hii i am first")
        label.pack()
win.mainloop()
