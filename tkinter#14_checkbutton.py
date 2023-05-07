from tkinter import*
win=Tk()
win.geometry("300x300")
w=Label(win,text="abhishek",fg='blue',font='100')
w.pack()

Checkbutton1=IntVar()
Checkbutton2=IntVar()
Checkbutton3=IntVar()

Button1=Checkbutton(win,text="about us ",variable=Checkbutton1,onvalue=1,offvalue=0,height=2,width=10)


Button2=Checkbutton(win,text="contact  ",variable=Checkbutton2,onvalue=1,offvalue=0,height=2,width=10)



Button3=Checkbutton(win,text="tutorials",variable=Checkbutton3,onvalue=1,offvalue=0,height=2,width=10)

Button1.pack()
Button2.pack()
Button3.pack()
mainloop()
