import mysql.connector
from StockDAO import stockDAO
import csv

mydb= mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Hei20041",
        # database = "datarepresentation",
        # auth_plugin='mysql_native_password'
        )

myCursor = mydb.cursor()

# create database
# sql= "DROP DATABASE shop" # overwrites existing database
myCursor.execute("DROP DATABASE IF EXISTS shop")
myCursor.execute("CREATE DATABASE shop")
# mydb.commit()
print("Database Created")
myCursor.execute("USE shop")
# create stock table
myCursor.execute("DROP TABLE IF EXISTS stock")
myCursor.execute("CREATE TABLE stock(id int AUTO_INCREMENT PRIMARY KEY, Type VARCHAR(15), Title VARCHAR(255), Artist_Author VARCHAR(255), Genre VARCHAR(25), Quantity int, Price double, Discogs_GoodReadsID VARCHAR(25))")
print("Create table")


# import stock from stock.csv
# convert each row into a tuple
with open("stock.csv") as f:
    stock = [tuple(line) for line in csv.reader(f)]


# sql = "insert into stock (Artist, Genre, Price, Quantity, Title, Type) values (%s, %s,%s, %s, %s, %s)"


# populate stock table from stock list
sql = "insert into stock (Type, Title, Artist_Author, Genre, Quantity, Price, Discogs_GoodReadsID) values (%s, %s,%s, %s, %s, %s, %s)"
for item in stock[1:]: # i.e all tuples in stock except the header line
    # values = (tuple(list(item.values())))
    myCursor.execute(sql, item)
    mydb.commit()