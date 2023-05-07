from tkinter import*
win=Tk()
win.geometry("400x250")
username=Label(win,text='username').place(x=30,y=50)
password=Label(win,text='password').place(x=30,y=90)
submitbutton=Button(win,text='submit',activebackground='red',activeforeground='blue').place(x=30,y=120)
a=Entry(win,width=20).place(x=100,y=50)
b=Entry(win,width=20).place(x=100,y=90)
win.mainloop()
