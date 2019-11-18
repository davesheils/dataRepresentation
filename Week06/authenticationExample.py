import requests
import json

# f = open("filename")
# file = f.read()

apiKey = '0c476a73bb3b6196bcc6c735e04d9d7eb87ddb12'
url= 'https://github.com/davesheils/dataRepresentation'

# putting the API key in the API key as data

#data = {'file':file, 'apikey':apikey}
# for public information
# response = requests.post(url, json = data)
# for private information
response = requests.get(url,auth=('davesheils',apiKey))

repoJSON = response.json()

filename = "repo.json"

file = open(filename, 'w')
json.dump(repoJSON, file, indent = 4)



