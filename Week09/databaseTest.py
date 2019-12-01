import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Hei20041",
    database = "datarepresentation",
    auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

# mycursor.execute("create DATABASE datarepresentation")

# sql = "CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)"
# mycursor.execute(sql)
# CRUD operations on the database tables

# create using SQL command insert. NB: note values are inserted seperately from the SQl

# sql = "insert into student (name, age) values (%s, %s)"
# adding multiple students
# students = [("Mary", 22), ("Grainne",35),("Manila",36),("Maya",35),("Simon",57),("David",50),("Helen",64)]
# for student in students:
#    mycursor.execute(sql, student)
#    mydb.commit() # Every CRUD operation must be committed

# print("students added to student table")

# Reading students from the database - all students

# sql = "select * from student" #sql
# mycursor.execute(sql) # execute command
# result = mycursor.fetchall() # fetchall
# print(result) # print result in the form of a list of tuples. could this be jsonified/dictionarified
# for record in result: # iterrate through result 
#    print(record[1], ", ", record[2])

# Reading students from the database - filtering

# sql = "select * from student where age > %s" #sql
# values = (30,) # even a single value must be in tuple format
# mycursor.execute(sql, values) # execute command
# result = mycursor.fetchall() # fetchall
# for record in result: # iterrate through result 
#    print(record)

# Update
# sql = "update student set age = %s where id = 8" #sql
# values = (17,) # Update Johanns age - check in mysql terminal 
# mycursor.execute(sql, values) # execute command
# mydb.commit()

# Delete
# remove David from the table
sql = "delete from student where name = %s" #sql
values = ("David",)
mycursor.execute(sql, values) # execute command
mydb.commit()