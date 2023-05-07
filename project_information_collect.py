from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def insert():
    id=e_id.get()
    name=e_name.get()
    phone=e_phone.get()

    if(id=="" or name=="" or phone==""):
        MessageBox.showinfo("Insert Status","All Fielfs are regquired")
    else:
        conn= mysql.connect(host='localhost', user='root', password="1111",database="ssm")
        cur=conn.cursor()
        cur.execute("INSERT INTO student VALUES('"+ id+ "','"+ name +"','"+ phone +"')")
        conn.commit()

        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_phone.delete(0,'end')
        show()
        MessageBox.showinfo("Insert Status","Inserted Successfully")
        conn.close()
        
def delete():
    id=e_id.get()
    name=e_name.get()
    phone=e_phone.get()
    
    if(e_id.get()==""):
        MessageBox.showinfo("Delete Status","ID required for delete")
    else:
        
        conn= mysql.connect(host='localhost', user='root', password="",
                            port=3307,
                            database="shishir")
        cur=conn.cursor()
        cur.execute("DELETE FROM student WHERE roll='"+ e_id.get() +"'")
        conn.commit()

        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_phone.delete(0,'end')
        show()
        MessageBox.showinfo("Delete Status","Delete Successfully")
        conn.close()
        
def update():
    id=e_id.get()
    name=e_name.get()
    phone=e_phone.get()

    if(id=="" or name=="" or phone==""):
        MessageBox.showinfo("Update Status","All Fielfs are regquired")
    else:
        conn= mysql.connect(host='localhost', user='root', password="",
                            port=3307,
                            database="shishir")
        cur=conn.cursor()
        cur.execute("UPDATE student SET name='"+ name +"', class='"+ phone +"' WHERE roll='"+ id +"'")
        conn.commit()

        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_phone.delete(0,'end')
        show()
        MessageBox.showinfo("Update Status","Updateed Successfully")
        conn.close()
        
def get():
    id=e_id.get()
    name=e_name.get()
    phone=e_phone.get()
    
    if(e_id.get()==""):
        MessageBox.showinfo("Fetch Status","ID required for Show")
    else:
        
        conn= mysql.connect(host='localhost', user='root', password="",
                            port=3307,
                            database="shishir")
        cur=conn.cursor()
        cur.execute("SELECT * FROM student WHERE roll='"+ e_id.get() +"'")
        rows=cur.fetchall()

        for row in rows:
            e_name.insert(0,row[1])
            e_phone.insert(0,row[2])
            
        conn.commit()

      
        MessageBox.showinfo("Fetch Status"," Successfully")
        conn.close()

def show():
    
    conn= mysql.connect(host='localhost', user='root', password="",
                            port=3307,
                            database="shishir")
    cur=conn.cursor()
    cur.execute("SELECT * FROM student")
    rows=cur.fetchall()
    list.delete(0, list.size())
    for row in rows:
        insertData= str(row[0])+'         '+ row[1] +'        '+ row[2]
        list.insert(list.size()+1, insertData)
    conn.close()
    
root=Tk()
root.geometry("600x500")
root.title("Shishir Kant Singh")

id=Label(root,text="Enter ID", font=('bold',10))
id.place(x=20, y=30)

name=Label(root,text="Enter Name", font=('bold',10))
name.place(x=20, y=60)

phone=Label(root,text="Enter Phone", font=('bold',10))
phone.place(x=20, y=90)

e_id=Entry()
e_id.place(x=150, y=30)

e_name=Entry()
e_name.place(x=150, y=60)

e_phone=Entry()
e_phone.place(x=150, y=90)

insert= Button(root, text="Insert", font=("italic", 10), bg="white", command=insert)
insert.place(x=20, y=140)

delete= Button(root, text="Delete", font=("italic", 10), bg="white", command=delete)
delete.place(x=70, y=140)

update= Button(root, text="Update", font=("italic", 10), bg="white", command=update)
update.place(x=120, y=140)

get= Button(root, text="Get", font=("italic", 10), bg="white", command=get)
get.place(x=170, y=140)

list=Listbox(root)
list.place(x=290,y=30)
show()

root.mainloop()
