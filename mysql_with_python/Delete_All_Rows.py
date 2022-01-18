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
sql = "DELETE FROM Table_name "
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

#================================================================
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
sql = "DELETE FROM my_detailes"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")
