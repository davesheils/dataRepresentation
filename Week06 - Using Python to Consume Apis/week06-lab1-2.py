import requests
import json
import urllib.parse
from xlwt import *

w = Workbook()
ws = w.add_sheet('cars')

w.save("cars.xls")

row = 0 # start at row 0

write table header
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

