from tkinter import*
win=Tk()
def hello():
    print("hii abhi")

menubar=Menu(win)
menubar.add_command(label="hi alok",command=hello)
menubar.add_command(label="Quit",command=win.quit)

win.config(menu=menubar)

win.mainloop()
