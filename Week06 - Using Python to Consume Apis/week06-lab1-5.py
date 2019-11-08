import requests
import json
import urllib.parse
from xlwt import *

url = "https://api.github.com/users/andrewbeattycourseware/followers"

response = requests.get(url)
data = response.json()

# write data to JSON file (neatly)
# file = open("andrewsFollowers.json", 'w')
# json.dump(data, file, indent=4)

for user in data:
    print(user['login'])

#for user in data:
#    file.write(user)

# adapt code from previous program to write data to excel
# selected keys only, for proof of concept

w = Workbook()
ws = w.add_sheet('followers')

w.save("andrewsFollowers.xls")

row = 0 # start at row 0

# write table header
ws.write(row,0,"login")
ws.write(row,1,"id")
ws.write(row,2,"url")
ws.write(row,3,"type")
ws.write(row,4,"site_admin")

# write data

row = 1

for user in data:
    ws.write(row,0,user["login"])
    ws.write(row,1,user["id"])
    ws.write(row,2,user["url"])
    ws.write(row,3,user["type"])
    ws.write(row,4,user["site_admin"])
    row += 1

w.save("andrewsFollowers.xls")