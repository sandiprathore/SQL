# Insert multiple values in mysql database table

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
sql = "INSERT INTO DB_name.Table_name (column_1,column_2,column_3,column_4) VALUES (%s,%s,%s,%s)"
val =[
('value_for_column_1','value_for_column_2','value_for_column_3','value_for_column_4'), # row 1
('value_for_column_1','value_for_column_2','value_for_column_3','value_for_column_4'), # row 2
('value_for_column_1','value_for_column_2','value_for_column_3','value_for_column_4')  # row 3 
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

#=======================================================================
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
sql = "INSERT INTO my_detailes (name,fathers_name,age,contect_no) VALUES (%s,%s,%s,%s)"
val =[
('Ravi rathore','Jagdish rathore',21,'78286940'),
('Atul yadaw','Rajesh yadaw',21,'90090568'),
('Roshani patel','Madan patel',45,'90090258')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")
