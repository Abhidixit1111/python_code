from tkinter import *
import pywhatkit  # for online edit it.
import tkinter.messagebox as MessageBox
import mysql.connector as mysql


conn= mysql.connect(host='localhost',user='root',password='1111',database='portal')
cur=conn.cursor()
def save():
    a=enrollment.get()
    b=name.get()
    c=father.get()
    d=month.get()
    f=phone.get()
    g=classs.get()
    h=otherfee.get()
    i=to.get()
    
    
    if(a=="" or b=="" or c=="" or d==""  or f=="" or g=="" or h=="" or i=="" ):
        MessageBox.showinfo("Insert Status","All Fields are required")
    else:
        conn= mysql.connect(host='localhost', user='root', password="1111",
    
                            database="portal")
        cur=conn.cursor()
        cur.execute("INSERT INTO student_fee VALUES('"+ a + "','"+ b +"','"+ c +"','"+ d +"','"+ f +"','"+ g +"','"+ h +"','"+ i +"')")
        conn.commit()

        enrollment.delete(0,'end')
        name.delete(0,'end')
        father.delete(0,'end')
        month.delete(0,'end')
        phone.delete(0,'end')
        classs.delete(0,'end')
        otherfee.delete(0,'end')
        to.delete(0,'end')
        show()
        MessageBox.showinfo("Insert Status","Inserted Successfully")
        conn.close()

        
      
def update():
    a=enrollment.get()
    b=name.get()
    c=father.get()
    d=month.get()
    f=phone.get()
    g=classs.get()
    h=otherfee.get()
    i=to.get()
    
    
    if(a=="" or b=="" or c=="" or d==""  or f=="" or g=="" or h=="" or i=="" ):
        MessageBox.showinfo("Update Status","All Fields are required")
    else:
        conn= mysql.connect(host='localhost', user='root', password="1111",
                            
                            database="portal")
        cur=conn.cursor()
        cur.execute("UPDATE student_fee SET b='"+ b +"', c='"+ c +"', d='"+ d +"', f='"+ f +"', g='"+ g +"', h='"+ h +"', i='"+ i +"' WHERE a='"+ a +"'")
        conn.commit()

        enrollment.delete(0,'end')
        name.delete(0,'end')
        father.delete(0,'end')
        month.delete(0,'end')
        phone.delete(0,'end')
        classs.delete(0,'end')
        otherfee.delete(0,'end')
        to.delete(0,'end')
        show()
        MessageBox.showinfo("Update Status","Updateed Successfully")
        conn.close()
    

def enquiry():
    a=enrollment.get()
    b=name.get()
    c=father.get()
    d=month.get()
    f=phone.get()
    g=classs.get()
    h=otherfee.get()
    i=to.get()
    
    if(enrollment.get()==""):
        MessageBox.showinfo("Fetch Status","ID required for Show")
    else:
        
        conn= mysql.connect(host='localhost', user='root', password="1111",
                            
                            database="portal")
        cur=conn.cursor()
        cur.execute("SELECT * FROM student_fee WHERE a='"+ enrollment.get() +"'")
        rows=cur.fetchall()

        for row in rows:
            name.insert(0,row[1])
            father.insert(0,row[2])
            month.insert(0,row[3])
            phone.insert(0,row[4])
            classs.insert(0,row[5])
            otherfee.insert(0,row[6])
            to.insert(0,row[7])
            
        conn.commit()

      
        MessageBox.showinfo("Fetch Status"," Successfully")
        conn.close()

    

def show():
    
    conn= mysql.connect(host='localhost', user='root', password="1111",
                            
                            database="portal")
    cur=conn.cursor()
    cur.execute("SELECT * FROM student_fee")
    rows=cur.fetchall()
    list.delete(0, list.size())
    for row in rows:
        insertData= str(row[0])+'        '+row[1] +'     '+row[2] +'     '+row[3] +'      '+row[4] +'     '+row[5] +'     '+row[6] +'     '+ row[7] 
        list.insert(list.size()+1, insertData)
        conn.close()


screen = Tk()
screen.title("fees")
screen.geometry("800x800")
screen.resizable(False,True)


Label(screen ,text='Student Fees Submission Portal', font='cambria 23 bold', bg='blue', fg='white',bd=7,relief=RIDGE).pack(fill='both')
Label(screen ,text="", font='cambria 1000 bold', bg='black', fg='white').pack(fill='both')


a=Label(screen, text='Enrollment No:',bg='black',fg='white',font='cambria 15 bold').place(x=40, y=80)
b=Label(screen, text='Name:',bg='black',fg='white',font='cambria 15 bold').place(x=40, y=130)
c=Label(screen, text='Fathers Name:',bg='black',fg='white',font='cambria 15 bold').place(x=40, y=180)
d=Label(screen, text='Month:',bg='black',fg='white', font='cambria 15 bold').place(x=40, y=230)
e=Label(screen, text='Hrr:',bg='black',fg='white',font='cambria 15 bold').place(x=40, y=280)
f=Label(screen, text='PHONE:',bg='black',fg='white',font='cambria 15 bold').place(x=440, y=80)
g=Label(screen, text='Class:',bg='black',fg='white',font='cambria 15 bold').place(x=440, y=130)
h=Label(screen, text='Other Fee:',bg='black',fg='white',font='cambria 15 bold').place(x=440, y=180)
i=Label(screen, text='To:',bg='black',fg='white',font='cambria 15 bold').place(x=440, y=230) 
j=Label(screen, text='Mm:',bg='black',fg='white',font='cambria 15 bold').place(x=440, y=280)


enrollment = Entry(screen, font='10', bd = 1)
enrollment.place(x=210,y=80)
name = Entry(screen, font='10', bd = 1)
name.place(x=210,y=130)
father = Entry(screen, font='10', bd = 1)
father.place(x=210,y=180)
month=Entry(screen, font='10', bd = 1)
month.place(x=210,y=230)
HR= Entry(screen, font='10', bd = 1)
HR.place(x=210,y=280)
phone = Entry(screen, font='10', bd = 1)
phone.place(x=550,y=80)
classs = Entry(screen, font='10', bd =1)
classs.place(x=550,y=130)
otherfee = Entry(screen, font='10', bd = 1)
otherfee.place(x=550,y=180)
to = Entry(screen, font='10', bd = 1)
to.place(x=550,y=230)
MM = Entry(screen, font='10', bd = 1)
MM.place(x=550,y=280)





def total():
    if(month.get()=='january'):
        x=1
    elif(month.get()=='febuary'):
        x=2
    elif(month.get()=='march'):
        x=3
    elif(month.get()=='april'):
        x=4
    elif(month.get()=='may'):
        x=5
    elif(month.get()=='june'):
        x=6
    elif(month.get()=='july'):
        x=7
    elif(month.get()=='august'):
        x=8
    elif(month.get()=='september'):
        x=9
    elif(month.get()=='octuber'):
        x=10
    elif(month.get()=='november'):
        x=11
    elif(month.get()=='december'):
        x=12
    else:
        print("please check the spelling!")

    
    if(to.get()=='january'):
        y=1
    elif(to.get()=='febuary'):
        y=2
    elif(to.get()=='march'):
        y=3
    elif(to.get()=='april'):
        y=4
    elif(to.get()=='may'):
        y=5
    elif(to.get()=='june'):
        y=6
    elif(to.get()=='july'):
        y=7
    elif(to.get()=='august'):
        y=8
    elif(to.get()=='september'):
        y=9
    elif(to.get()=='octuber'):
        y=10
    elif(to.get()=='november'):
        y=11
    elif(to.get()=='december'):
        y=12
    else:
        print("please check the spelling!")
    if(x>y):
        x,y=y,x
        y=y+6
    z=y-x+1
    z=z*1000
    o=int(otherfee.get())
    z=z+o
    z=str(z)
    MessageBox.showinfo("IMPORTANT",'TOTAL FEE='+z)
    return z

def send():
    n=name.get()
    x='+91'+phone.get()
    y=int(HR.get())
    z=int(MM.get())+1
    msg='your kid '+n+' has submitted his fee'
    pywhatkit.sendwhatmsg(x,msg,y,z)




save=Button(screen, text=".   SAVE    .", font='cambria 14 bold',bg='blue',fg='white', bd=0,activebackground="green",command=save)
save.place(x=40,y=350)
enquiry=Button(screen, text='Enquiry', font='cambria 14 bold',bg='blue',fg='white',bd=0,activebackground="green",command=enquiry)
enquiry.place(x=200, y=350)
update=Button(screen, text='Update', font='cambria 14 bold',bg='blue',fg='white',bd=0,activebackground="green",command=update)
update.place(x=350, y=350)
send=Button(screen, text="Send Message", font='cambria 14 bold',bg='blue',fg='white',bd=0,activebackground="green",command=send)
send.place(x=600,y=350)

total=Button(screen, text="total", font='cambria 14 bold',bg='blue',fg='white',bd=0,activebackground="green",command=total)
total.place(x=500,y=350)



list=Listbox(screen,width=115 ,height=15,bd=1)
list.place(x=40,y=420)
show()



screen.mainloop()
