import requests
import json
import urllib.parse

url = "http://127.0.0.1:5000/cars"

# 1. Get cars from the server (as function), and printing individually
def getcars():
    url = "http://127.0.0.1:5000/cars"
    response = requests.get(url)
    data = response.json()
    # (a) prints cars to screen
    # printing cars individually
    return data['cars']
  

cars = getcars()
for car in cars:
    print(car)

# writing the JSON neatly to a file

file = open("cars.json", 'w')

json.dump(data, file, indent=4)

# write the cars to an excel file (row by row)

from xlwt import *

w = Workbook()
ws = w.add_sheet('cars')

w.save("cars.xls")

row = 0 # start at row 0

# write table header
ws.write(row,0,"reg")
ws.write(row,1,"make")
ws.write(row,2,"model")
ws.write(row,3,"price")

# start writing cars to spreadsheet, starting at row 1

row = 1

for car in cars:
    ws.write(row,0,car['reg'])
    ws.write(row,1,car['make'])
    ws.write(row,2,car['model'])
    ws.write(row,3,car['price'])
    row +=1

w.save('cars.xls')

# 2. Create a car on the server using the api

newCar = {'reg':'07 MH 1234', 'make':'Ford', 'model':'Fiesta','price':6500}

urlReg = url + "/" + urllib.parse.quote(newCar["reg"])

data = json.dumps(newCar)

print(urlReg)

r = requests.post(url, json=newCar)

# 3 update car on the server

# this was my first attempt ... didn't work


# updateCar = {'reg':'181 G 1234', 'make':'Ford', 'model':'Fidelma','price':10000}
# urlReg = url + "/" + urllib.parse.quote(updateCar["reg"])
# print(urlReg)
# r = requests.put(url, json=updateCar)

# Anthony's solution ...

dataString = {'make':'Ford','model':'Kuga'}
ulrReg = 'http://127.0.0.1:5000/cars/test'

response  = requests.put(ulrReg, json=dataString)
print(response.status_code)
print(response.text)

print(getcars())

# needless to say, this doesn't work, just like the AJAX version

# 4 delete the Fiesta from the cars list ...
# reuse the urllib.parse function to create the url

reg = '07 MH 1234'
urlReg = url + "/" + urllib.parse.quote(reg)
print(urlReg)


r = requests.delete(urlReg)

# This works

cars = getcars()
for car in cars:
    print(car)

