import mysql.connector
abhi=mysql.connector.connect(host='localhost',
                             user='root',
                             password='abhisheksql1111',
                             database='ssm')
xyz=abhi.cursor()
a="INSERT INTO student(name,roll_no,sec) VALUES('abhishek',21,'d')"
xyz.execute(a)
abhi.commit()
