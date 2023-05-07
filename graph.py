from tkinter import*
win=Tk()
win.geometry("500x500")
def abc():
    for i in range(360):
        can.create_arc(100,100,300,300,start=0,extent=i,fill="blue")
        can.update_idletasks()
can=Canvas(win,width='400',height='400',bg='orange')
cord=100,100,300,300
line=can.create_rectangle(cord,fill="red")
can.pack()
Button(win,text="click",command=abc).pack()
win.mainloop()
