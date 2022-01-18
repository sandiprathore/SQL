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
mycursor.execute("""ALTER TABLE table_name 
                    RENAME COLUMN old_column_name 
                    TO new_column_name;""")

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
mycursor = mydb.cursor()
mycursor.execute("""ALTER TABLE my_detailes 
                    RENAME COLUMN age_of_intern 
                    TO age;""")
                    