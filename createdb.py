import mysql.connector

abhi=mysql.connector.connect(host='localhost',
                             user='root',
                             password='abhisheksql1111')

abc=abhi.cursor()
abc.execute("CREATE DATABASE ssm")

