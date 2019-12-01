# Data Access Object Pattern or DAO pattern is used to separate low level data accessing API or operations from high level business services. Following are the participants in Data Access Object Pattern.
# Data Access Object Interface - This interface defines the standard operations to be performed on a model object(s).
# Data Access Object concrete class - This class implements above interface. This class is responsible to get data from a data source which can be database / xml or any other storage mechanism.
# Model Object or Value Object - This object is simple POJO containing get/set methods to store data retrieved using DAO class.

import mysql.connector

class StudentDAO:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Hei20041",
        database = "datarepresentation",
        auth_plugin='mysql_native_password'
        )
    
    def create(self, values):
        cursor = self.db.cursor()
        sql = "insert into student (name, age) values (%s, %s)"
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = "select * from student"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    def getByID(self, id):
        cursor = self.db.cursor()
        sql = "select * from student where id = %s"
        values = (id,)
        cursor.execute(sql,values)
        result = cursor.fetchone()
        return result

    def update(self, values):
        cursor = self.db.cursor()
        sql = "update student set name = %s, age = %s where id = %s"
        cursor.execute(sql,values)
        self.db.commit()
    
    def delete(self, id):
        cursor = self.db.cursor()
        sql = "delete from student where id = %s"
        value = (id,)
        cursor.execute(sql, value)
        self.db.commit()
        print("delete executed")

studentDAO = StudentDAO()
studentDAO.delete(17)