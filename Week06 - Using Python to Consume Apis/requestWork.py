import requests

# print (requests.__file__) 

# url = 'https://www.hea.ie'

# response = requests.get(url)

# print(response.status_code)
# print(response.text)
# print(response.headers)

# start restserver before getting next section working

url = 'http://127.0.0.1:5000/cars'
data = {'reg':'06 LH 1862', 'make':'Toyota', 'model':'Yaris', 'price':6500}


response = requests.post(url, json=data)

print(response.status_code)
print(response.json())