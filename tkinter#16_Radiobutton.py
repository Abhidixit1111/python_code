from tkinter import*
from tkinter.ttk import*
win=Tk()
win.geometry("400x400")
v=StringVar(win,'1')

option={"Option A":"1",
        "Option B":"2",
        "Option C":"3",
        "Option D":"4",
        }

style=Style(win)
style.configure("TRadiobutton",background="blue",foreground="yellow",font=("arial",14,"bold"))
values={"RadipButton 1":"1",
        "RadipButton 2":"2",
        "RadipButton 3":"3",
        "RadipButton 4":"4",
        }

for(txt,val)in option.items():
    Radiobutton(win,text=txt,variable=v,value=val).pack(side=TOP,ipady=4)

for(text,values)in values.item():
    Radiobutton(win,text=text,variable=v,value=value).pack(side=LEFT,ipady=4)
    
mainloop()
win.mainloop()

