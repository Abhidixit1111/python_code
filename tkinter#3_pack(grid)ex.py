import tkinter as tk
win=tk.Tk()

frame=tk.Frame(master=win,relief=tk.RAISED,borderwidth=2)
frame.grid(row=1,column=1,padx=5,pady=5)
label=tk.Label(master=frame,text=f"hiii")
label.pack()


frame=tk.Frame(master=win,relief=tk.RAISED,borderwidth=2)
frame.grid(row=2,column=2,padx=5,pady=5)
label=tk.Label(master=frame,text=f"hlo")
label.pack()

frame=tk.Frame(master=win,relief=tk.RAISED,borderwidth=2)
frame.grid(row=3,column=3,padx=5,pady=5)
label=tk.Label(master=frame,text=f"hey")
label.pack()
win.mainloop()
