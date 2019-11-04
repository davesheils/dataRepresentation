
import requests
import csv
from bs4 import BeautifulSoup


# connect to and get html of myhome page - Dublin 18 residential sales
page = requests.get("https://www.myhome.ie/residential/mayo/property-for-sale")
soup = BeautifulSoup(page.content, 'html.parser') ## reads web page and converts to a DOM tree

home_file = open('week03MyHome.csv', mode = 'w')

home_writer = csv.writer(home_file, delimiter = '\t', quotechar = '"', quoting = csv.QUOTE_MINIMAL)

home_writer.writerow(["Price","Address"])

listings = soup.findAll("div", class_ = "PropertyListingCard")

# print(listings)

for listing in listings:
    entryList = []

    price = listing.find(class_="PropertyListingCard__Price").text
    entryList.append(price)
    address = listing.find(class_="PropertyListingCard__Address").text
    # print(address)
    entryList.append(address)

    home_writer.writerow(entryList)

home_file.close()