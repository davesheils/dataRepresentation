import requests
import json

# 1 - 2 

f = open("/home/david/Dropbox/HDip in Data Analytics/Semester 4/Data Representation/dataRepresentation/week02-JavaScript/carViewerV1.html")
html = f.read()

# print(file)

# using my own api key

apiKey = 'd5297bb6de1098e8aa85fec9c683892cf089965ac66d53fdc9d62df224bee340'
url= 'https://api.html2pdf.app/v1/generate'
#filename = "repo.json"

# putting the API key in the API key as data

data = {'html':html, 'apiKey':apiKey}
# for public information
response = requests.post(url, json = data)

print(response.status_code)

# response = response.json()

carViewerPDF = open("carViewer.pdf", "wb") #  wb = write binary
# json.dump(repoJSON, file, indent = 4)
carViewerPDF.write(response.content)