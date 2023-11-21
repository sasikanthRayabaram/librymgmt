import mysql.connector

myconn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="bannu"
)

mycursor=myconn.cursor()
mycursor.execute#(write operation query)

