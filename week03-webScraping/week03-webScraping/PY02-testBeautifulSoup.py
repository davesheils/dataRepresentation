import requests
from bs4 import BeautifulSoup
# lab1 = Car Viewer without javascript
with open("lab1.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

print(soup.prettify())