import mysql.connector
abhi=mysql.connector.connect(host='localhost',
                           user='root',
                           password='abhisheksql1111',
                           database='ssm')
xyz=abhi.cursor()
s="CREATE TABLE student(name varchar(20),roll_no integer(4),sec varchar(5))"
xyz.execute(s)
