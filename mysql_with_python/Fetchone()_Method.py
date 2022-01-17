
# fetchone method is only for print the first row of mysql databse table 

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
mycursor.execute("SELECT * FROM Table_name")
myresult = mycursor.fetchone()
print(myresult)

#===============================================================

# Example 

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
myresult = mycursor.fetchone()
print(myresult)

