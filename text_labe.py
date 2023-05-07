from tkinter import*
win=Tk()
win.geometry("400x400")
frame2=win.Label(win,text="hello i am abhishek")
frame1=win.Frame(master=win,height="400",width="400",bg="red")
frame2.pack()
win.title('AD')
win.geometry("200x200+10+20")
win.mainloop()
