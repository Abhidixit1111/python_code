import mysql.connector

abhi=mysql.connector.connect(host='localhost',
                             user='root',
                             password='abhisheksql1111')

if abhi.is_connected():
    print("connnection is successful")

else:
    print("connection is not successful")
