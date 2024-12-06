
JUPYTER
FAQ
#Proprietary content. © Great Learning. All Rights Reserved. Unauthorized use or distribution prohibited.
conda install -c anaconda mysql-connector-python
Python needs a MySQL driver to access the MySQL database.
!pip install  mysql-connector-python
Requirement already satisfied: mysql-connector-python in c:\users\sampriti\anaconda3\lib\site-packages (8.0.21)
Requirement already satisfied: protobuf>=3.0.0 in c:\users\sampriti\anaconda3\lib\site-packages (from mysql-connector-python) (3.13.0)
Requirement already satisfied: six>=1.9 in c:\users\sampriti\anaconda3\lib\site-packages (from protobuf>=3.0.0->mysql-connector-python) (1.15.0)
Requirement already satisfied: setuptools in c:\users\sampriti\anaconda3\lib\site-packages (from protobuf>=3.0.0->mysql-connector-python) (49.2.0.post20200714)
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="12345678"
)

print(mydb)
<mysql.connector.connection.MySQLConnection object at 0x000001F66360A850>
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="sq"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="sq"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

print(mycursor)

for x in mycursor:
  print(x)
MySQLCursor: SHOW TABLES
('customers',)
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
1 record inserted.
mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
13 was inserted.
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
('John', 'Highway 21', 1)
('Peter', 'Lowstreet 4', 2)
('Amy', 'Apple st 652', 3)
('Hannah', 'Mountain 21', 4)
('Michael', 'Valley 345', 5)
('Sandy', 'Ocean blvd 2', 6)
('Betty', 'Green Grass 1', 7)
('Richard', 'Sky st 331', 8)
('Susan', 'One way 98', 9)
('Vicky', 'Yellow Garden 2', 10)
('Ben', 'Park Lane 38', 11)
('William', 'Central st 954', 12)
('Chuck', 'Main Road 989', 13)
('Viola', 'Sideway 1633', 14)
mycursor = mydb.cursor()

mycursor.execute("SELECT count(*) FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
(14,)
mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
('Ben', 'Park Lane 38', 11)
mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
('John', 'Highway 21', 1)
('Susan', 'One way 98', 9)
('Viola', 'Sideway 1633', 14)
mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
('Amy', 'Apple st 652', 3)
('Ben', 'Park Lane 38', 11)
('Betty', 'Green Grass 1', 7)
('Chuck', 'Main Road 989', 13)
('Hannah', 'Mountain 21', 4)
('John', 'Highway 21', 1)
('Michael', 'Valley 345', 5)
('Peter', 'Lowstreet 4', 2)
('Richard', 'Sky st 331', 8)
('Sandy', 'Ocean blvd 2', 6)
('Susan', 'One way 98', 9)
('Vicky', 'Yellow Garden 2', 10)
('Viola', 'Sideway 1633', 14)
('William', 'Central st 954', 12)
mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
('William', 'Central st 954', 12)
('Viola', 'Sideway 1633', 14)
('Vicky', 'Yellow Garden 2', 10)
('Susan', 'One way 98', 9)
('Sandy', 'Ocean blvd 2', 6)
('Richard', 'Sky st 331', 8)
('Peter', 'Lowstreet 4', 2)
('Michael', 'Valley 345', 5)
('John', 'Highway 21', 1)
('Hannah', 'Mountain 21', 4)
('Chuck', 'Main Road 989', 13)
('Betty', 'Green Grass 1', 7)
('Ben', 'Park Lane 38', 11)
('Amy', 'Apple st 652', 3)
 
This website does not host notebooks, it only renders notebooks available on other websites.

Delivered by Fastly, Rendered by OVHcloud

nbviewer GitHub repository.

nbviewer version: 51eff7b

nbconvert version: 7.2.3

Rendered a few seconds ago
