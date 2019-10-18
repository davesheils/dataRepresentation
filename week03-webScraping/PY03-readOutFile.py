import requests
from bs4 import BeautifulSoup
# lab1 = Car Viewer without javascript
with open("lab1.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

rows = soup.findAll("tr")
for row in rows:
    cols = row.findAll("td")
    dataList = []
    # need to modify following so that update and delete not added 
    for col in cols:
        dataList.append(col.text)
    print(dataList)


