<div id="top"></div>

## MYSQL Queries Run with python
* #### Table of Contents
  
  
1. <a href="#Prerequisite">Prerequisite</a>
2. <a href="#Download-and-install">Download and install "mysql connector"</a>
3. <a href="#Test-MySQL-Connector">Test MySQL Connector</a>
4. <a href="#Syntax-to-run-sql-queries-with-python">Syntax to run sql queries with python</a>
5. <a href="#Create-database">Create database</a>
6. <a href="#Connect-to-your-database">Show database</a>
7. <a href="#Create-table-to-your-database">Create table to your database</a>
8. <a href="#Insert-values-in-table">Insert single row in table</a>
9. <a href="#Insert-multiple-rows-in-table">Insert multiple rows in table</a>
10. <a href="#Print-table-data">Print table data</a>
10. <a href="#Delete-all-rows-from-table">Delete all  rows from table</a>
10. <a href="#Select-data-From-a-Table">Select data From a Table</a>
11. <a href="#Selecting-Columns">Select some Column from a table </a>
12. <a href="#Count-rows">Count rows in a table</a>
13. <a href="#fetchone()-Method">fetchone() Method</a>
14. <a href="#Select-where">Select where</a>
15. <a href="#Wildcard-Characters-(LIKE)">Wildcard Characters ( LIKE )</a>
16. <a href="#MySQL-Order-By">Order By ( sort the result in ascending order ) </a>
17. <a href="#ORDER-BY-DESC">ORDER BY DESC ( sort the result in descending order )</a>

<div id="Prerequisite"></div>

#### Prerequisite

* host name or id 
* uresname of mysql user 
* password of mysql user 
* port number 

<p align="right">(<a href="#top">back to top</a>)</p>


<div id="Download-and-install"></div>

#### Download and install "mysql connector"

```sh
pip install mysql-connector-python
```
<div id="Test-MySQL-Connector"></div>

  #### Test MySQL Connector
file name: test_cconector.py
```sh
import mysql.connector  
print("hello SQL")
```
Example : <a  href="https://github.com/sandiprathore/SQL/blob/mysql_with_python/mysql_with_python/Test_connector.py" target="_blank">Ref. and Example</a>

#### Output
```sh
hello SQL
```
<p align="right">(<a href="#top">back to top</a>)</p>  
<div id="Syntax-to-run-sql-queries-with-python"></div>

#### Syntax to run sql queries with python
Create python_script(file)→write your queries in it with correct syntax →run this file in terminal

###### To run mysql quiers you must have following details

* host name or id 
* uresname of mysql user 
* password of mysql user 
* port number


<!-- Create database -->
<div id="Create-database"></div>

#### Create database
File name: Create_DB.py
```sql
import mysql.connector
mydb = mysql.connector.connect(
  host="host",
  user="username",
  password="password",
  port=3306
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE DB_name ")
```
Example : <a  href="https://github.com/sandiprathore/SQL/blob/mysql_with_python/mysql_with_python/Create_DB.py" target="_blank">Ref. and Example</a>
<p  align="right">(<a href="#top">back to top</a>)</p>
<div id="Connect-to-your-database"></div>


<!-- Show database -->
 #### Show database
File name: Show_DB.py
```sql
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
```
Example : <a  href="https://github.com/sandiprathore/SQL/blob/mysql_with_python/mysql_with_python/Show_DB.py" target="_blank">Ref. and Example</a>
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- Create table to your database -->
<div id="Create-table-to-your-database"></div>

#### Create table to your database
File name: Create_table.py
```sql
import mysql.connector
mydb = mysql.connector.connect(
  host="host",
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
```
Example : <a  href="https://github.com/sandiprathore/SQL/blob/mysql_with_python/mysql_with_python/Create_table.py" target="_blank">Ref. and Example</a>
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- Insert single row in table -->
<div id="Insert-values-in-table"></div>

#### Insert single row in table

File name: Insert_single_row.py
```sql  
import mysql.connector
mydb = mysql.connector.connect(
  host="host",
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
```
Example : <a  href="https://github.com/sandiprathore/SQL/blob/mysql_with_python/mysql_with_python/Insert_single_row.py" target="_blank">Ref. and Example</a>
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- Insert multiple rows in table -->
<div id="Insert-multiple-rows-in-table"></div>

#### Insert multiple rows in table
File name: Insert_mulltiple_rows.py
  
```sql
import mysql.connector
mydb = mysql.connector.connect(
  host="host",
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
```
Example : <a  href="https://github.com/sandiprathore/SQL/blob/mysql_with_python/mysql_with_python/Insert_mulltiple_rows.py" target="_blank">Ref. and Example</a>
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- Print table data -->
<div id="Print-table-data"></div>

#### Print table data 
file name: Print_table.py
```sql
import mysql.connector
mydb = mysql.connector.connect(
  host="host",
  user="username",
  password="password",
  database="DB_name",
  port=3306
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM table_name")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
```
Example : <a  href="https://github.com/sandiprathore/SQL/blob/mysql_with_python/mysql_with_python/Print_table.py" target="_blank">Ref. and Example</a>
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- Delete all rows from table -->
<div id="Delete-all-rows-from-table"></div>

#### Delete all rows from table 
File name: Delete_all_rows.py
```sql
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

```
Example : <a  href="https://github.com/sandiprathore/SQL/blob/mysql_with_python/mysql_with_python/Delete_All_Rows.py" target="_blank">Ref. and Example</a>
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- Select data From a Table -->
<div id="Select-data-From-a-Table"></div>

#### Select data From a Table:
File name: select_data.py
```sql  
import mysql.connector
mydb = mysql.connector.connect(
  host="host",
  user="username",
  password="password",
  database="DB_name",
  port=3306
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM table_name")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)   
```
Example : <a  href="https://github.com/sandiprathore/SQL/blob/mysql_with_python/mysql_with_python/Select_data.py" target="_blank">Ref. and Example</a>
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- Select some Columns from a table -->
<div id="Selecting-Columns"></div>

#### Select some Columns from a table

File name: Select_column.py

```sql
import mysql.connector
mydb = mysql.connector.connect(
  host="host",
  user="username",
  password="password",
  database="DB_name",
  port=3306
)
mycursor = mydb.cursor()
mycursor.execute("SELECT column_name FROM table_name")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
```
Example : <a  href="https://github.com/sandiprathore/SQL/blob/mysql_with_python/mysql_with_python/Select_column.py" target="_blank">Ref. and Example</a>
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- Count rows in  a tbale -->
<div id="Count-rows"></div>

#### Count rows in  a tbale:

File name: Cout_rows.py

  
```sql
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
```
Example : <a  href="https://github.com/sandiprathore/SQL/blob/mysql_with_python/mysql_with_python/Cout_rows.py" target="_blank">Ref. and Example</a>
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- fetchone() Method -->
<div id="fetchone()-Method"></div>

#### fetchone() Method
If you are only interested in one row, you can use the fetchone() method.
The fetchone() method will return the first row of the result
File name: Fetchone()_Method.py
```sql
import mysql.connector
mydb = mysql.connector.connect(
  host="host",
  user="username",
  password="password",
  database="DB_name",
  port=3306
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Table_name")
myresult = mycursor.fetchone()
print(myresult)
```
Example : <a  href="https://github.com/sandiprathore/SQL/blob/mysql_with_python/mysql_with_python/Fetchone()_Method.py" target="_blank">Ref. and Example</a>
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Select where  -->
<div id="Select-where"></div>

#### Select where 
When selecting records from a table, you can filter the selection by using the "WHERE" statement:  

File_name: Select_where.py
```sql
import mysql.connector
mydb = mysql.connector.connect(
  host="host",
  user="username",
  password="password",
  database="DB_name",
  port=3306
)
mycursor = mydb.cursor()
sql = "SELECT * FROM Table_name WHERE column_name ='value'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
```
Example : <a  href="https://github.com/sandiprathore/SQL/blob/mysql_with_python/mysql_with_python/Select_where.py" target="_blank">Ref. and Example</a>
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- Wildcard Characters ( LIKE ) -->
<div id="Wildcard-Characters-(LIKE)""></div>

#### Wildcard Characters ( LIKE )
You can also select the records that starts, includes, or ends with a given letter or phrase.
Use the %  to represent wildcard characters:
import mysql.connector
file name: LIKE_Operator.py
```sql
import mysql.connector
mydb = mysql.connector.connect(
  host="host",
  user="username",
  password="password",
  database="DB_name",
  port=3306
)
mycursor = mydb.cursor()
sql = "SELECT * FROM Table_name WHERE column_1 LIKE '%Value%'" 
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
```
Example : <a  href="https://github.com/sandiprathore/SQL/blob/mysql_with_python/mysql_with_python/LIKE_Operator.py" target="_blank">Ref. and Example</a>
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MySQL Order By -->
 <div id="MySQL-Order-By"></div>

#### MySQL Order By
Sort the Result
Use the ORDER BY statement to sort the result in ascending or descending order.
The ORDER BY keyword sorts the result ascending by default

Filename: Order_by_shorting.py (ascending  order)
```sql
import mysql.connector
mydb = mysql.connector.connect(
  host="host",
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
```
Example : <a  href="https://github.com/sandiprathore/SQL/blob/mysql_with_python/mysql_with_python/Order_by_shorting.py" target="_blank">Ref. and Example</a>
 <p align="right">(<a href="#top">back to top</a>)</p>


 <!-- ORDER BY DESC -->
<div id="ORDER-BY-DESC"></div>

#### ORDER BY DESC 
Use the DESC keyword to sort the result in a descending order.
DESC keyword is use to short table table in reverse oprder
 File name: Order_bt(DESC).py
```sql 
import mysql.connector
mydb = mysql.connector.connect(
  host="host",
  user="username",
  password="password",
  database="DB_name",
  port=3306
) 
mycursor = mydb.cursor()
sql = """SELECT * FROM Table_name 
        ORDER BY name DESC"""
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
```
Example : <a  href="https://github.com/sandiprathore/SQL/blob/mysql_with_python/mysql_with_python/Order_bt(DESC).py" target="_blank">Ref. and Example</a>
<p align="right">(<a href="#top">back to top</a>)</p> 
