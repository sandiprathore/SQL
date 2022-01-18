# Syntax:

import mysql.connector
mydb = mysql.connector.connect(
  host="host",
  user="username",
  password="password",
  port=3306
)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)

#==================================================================
# Example

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="new_user",
  password="%sql1234",
  port=3306
)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)
  