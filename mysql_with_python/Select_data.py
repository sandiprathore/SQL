# Select table from mysql databse  
# syntax: 

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password",
  database="DB_name",
  port=3306
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM table_name")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#==============================================================
# Example:

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="new_user",
  password="%sql1234",
  database="my_database",
  port=3306
  )
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM my_detailes")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
