from studentDAO import studentDAO

# Testing CRUD functions
# CREATE
# studentDAO.create(("Zuzanna", 25))

# getByID()
# print(studentDAO.getByID(11))

# update
# newDetails = ("Mariana", 25, 11)
# studentDAO.update(newDetails)
# print(studentDAO.getByID(11))

# delete
for n in range(17,26):
    studentDAO.delete(n)

allStudents = studentDAO.getAll()
for student in allStudents:
    print(student)