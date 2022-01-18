# syntax:

import mysql.connector
mydb = mysql.connector.connect(
  host="host",
  user="username",
  password="password",
  database="DB_name"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT COUNT(*) FROM Table_name;")
myresult = mycursor.fetchone()
print(myresult)

#==========================================================================
# Example: 

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="new_user",
  password="%sql1234",
  database="my_database"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT COUNT(*) FROM my_detailes;")
myresult = mycursor.fetchone()
print(myresult)
