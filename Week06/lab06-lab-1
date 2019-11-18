import requests
import json
# import urllib.parse
# from xlwt import *

apiKey = "158cab8f7842107a1afb67a9036be9f7668167a9"
url = "https://github.com/davesheils/dataRepresentation"

response = requests.get(url,auth = ('davesheils', apiKey))

repoJSON = response.json()

filename = "Lab06.json"
file = open(filename, 'w')

json.dump(repoJSON, filename, indent=4)