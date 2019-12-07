import json
from StockDAO import stockDAO

import mysql.connector

mydb= mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Hei20041",
        database = "shop",
        # auth_plugin='mysql_native_password'
        )

myCursor = mydb.cursor()

data = {"Type":"Book","Title":"Days Without End","Artist_Author":"Barry, Sebastian","Genre":"Fiction","Quantity":10,"Price":10.99,"Discogs_GoodReadsID":""}

print("Data = ",data)

values = tuple(list(data.values()))


# values = (newItem['Type'],newItem['Title'],newItem['Artist_Author'],newItem['Genre'],newItem['Quantity'],newItem['Price'],newItem['Discogs_GoodReadsID'])

print("Values ", values)

sql = "insert into stock (Type, Title, Artist_Author, Genre, Quantity, Price, Discogs_GoodReadsID) values (%s, %s,%s, %s, %s, %s, %s)"
myCursor.execute(sql, values)
mydb.commit()

# print("newItem = ", newItem)

