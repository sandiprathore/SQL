 # Syntax:

import mysql.connector
mydb = mysql.connector.connect(
  host="host",
  user="username",
  password="password",
  database="DB_name",
  port=3306
)
mycursor = mydb.cursor()
sql = "SELECT * FROM Table_name WHERE column_1 LIKE '%Value%'"  #value = hiint
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
sql = "SELECT * FROM my_detailes WHERE name LIKE '%san%'"  
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
