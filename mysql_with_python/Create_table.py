# Create table in mysql using python  
#syntax:

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password",
  database="DB_name",
  port=3306
)
q="""
CREATE TABLE DB_name.Table_name
(
 column_1 DATATYPE(range), 
 column_2 DATATYPE(range),
 column_3 DATATYPE(range), 
 column_4 DATATYPE(range)
)
"""
mycursor = mydb.cursor()
mycursor.execute(q)
for x in mycursor:
  print(x)

#==============================================================
# Example

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="new_user",
  password="%sql1234",
  database="my_database",
  port=3306
)
q="""
CREATE TABLE my_database.my_detailes
(
 name VARCHAR(255), 
 fathers_name VARCHAR(255),
 age_of_intern int(50), 
 contect_no int(12)
)
"""
mycursor = mydb.cursor()
mycursor.execute(q)
for x in mycursor:
  print(x)

