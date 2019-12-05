# Data Access Object Pattern or DAO pattern is used to separate low level data accessing API or operations from high level business services. Following are the participants in Data Access Object Pattern.
# Data Access Object Interface - This interface defines the standard operations to be performed on a model object(s).
# Data Access Object concrete class - This class implements above interface. This class is responsible to get data from a data source which can be database / xml or any other storage mechanism.
# Model Object or Value Object - This object is simple POJO containing get/set methods to store data retrieved using DAO class.

import mysql.connector




class StockDAO:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Hei20041",
        database = "shop",
        auth_plugin='mysql_native_password'
        )

    def create(self, values):
        cursor = self.db.cursor()
        sql = "insert into stock (Type, Title, Artist_Author, Genre, Quantity, Price, Discogs_GoodReadsID) values (%s, %s,%s, %s, %s, %s, %s)"
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = "select * from stock"
        cursor.execute(sql)
        data = cursor.fetchall()
        stockList =[]
        for row in data:
            stockList.append(self.convertToDictionary(row))
        return stockList
    
    def getByID(self, id):
        cursor = self.db.cursor()
        sql = "select * from stock where id = %s"
        values = (id,)
        cursor.execute(sql,values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        # need to think about this one
        sql = "update stock set Type = %s, Title = %s Artist_Author = %s, Genre = %s, Quantity = %s, Price = %s, Discogs_GoodReadsID = %s where id = %s"
        cursor.execute(sql,values)
        self.db.commit()
    
    def delete(self, id):
        cursor = self.db.cursor()
        # likewise
        sql = "delete from stock where id = %s"
        value = (id,)
        cursor.execute(sql, value)
        self.db.commit()
        print("delete executed")
    def convertToDictionary(self, result):
        cols = ['id', 'Type', 'Title', 'Artist_Author',  'Genre',  'Quantity', 'Price', 'Discogs_GoodReadsID']
        item = {}
        if result:
            for i, col in enumerate(cols):
                value = result[i]
                item[col] = value
        return(item)

stockDAO = StockDAO()
# values = (stockDAO.getAll())
# for value in values:
#    print(value)