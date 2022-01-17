# Insert a single record in mysql databse table

# Syntax

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password",
  database="DB_name",
  port=3306
)
mycursor = mydb.cursor()
sql = "INSERT INTO DB_name.Table_name (column_1,column_2,column_3,column_4) VALUES (%s,%s,%s,%s)"
val =('value_for_column_1','value_for_column_2','value_for_column_3','value_for_column_4')
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

#==================================================================================
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
sql = "INSERT INTO my_database.my_detailes (name,fathers_name,age,contect_no) VALUES (%s,%s,%s,%s)"
val =('sanmdip rathore','jagdish rathore',21,'78286940')
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
