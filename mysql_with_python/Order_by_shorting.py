# The ORDER BY keyword is used to sort the result-set in ascending or descending order.
# Syntax:

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password",
  database="DB_name",
  port=3306
) 
mycursor = mydb.cursor()
sql = "SELECT * FROM Table_name ORDER BY value"
mycursor.execute(sql)
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
sql = """SELECT * FROM my_detailes 
        ORDER BY name"""
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

