import csv
from bs4 import BeautifulSoup

# lab1 is the name of the carviewer html file

with open("lab1.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

car_file = open('car_file.csv', mode = 'w')
car_writer = csv.writer(car_file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)

rows = soup.findAll("tr")
for row in rows:
    cols = row.findAll("td")
    dataList = []
    # need to modify following so that update and delete not added 
    for col in cols:
        # following line to exclude 'update' and 'delete' from output file
        if ((col.text !="delete") and (col.text !="update")):
            dataList.append(col.text)
    car_writer.writerow(dataList)


car_file.close()