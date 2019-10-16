# Read data from lab2.html (aka carViewer) and store data in csv

# do not add update or delete

# Import libraries

import requests
from bs4 import BeautifulSoup
import csv

# Connect to lab1.html
with open("lab1.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

# open csv file

car_file = open('car_file.csv', mode = 'w')
car_writer = csv.writer(car_file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)

# scrape data from table rows
rows = soup.findAll("tr")

for row in rows:
    cols = row.findAll("td")
    dataList = []
    # need to modify following so that update and delete not added 
    for col in cols:
        dataList.append(col.text)
    car_writer.writerow(dataList)

car_file.close()    

