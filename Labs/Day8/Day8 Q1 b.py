# 2. Sends custom headers with the request

import requests

url = "http://127.0.0.1:5000/users"

headers = {
    "User-Agent" : "Python-Client",
    "Accept" : "application/json"
}

response = requests.get(url,headers=headers)
print("Status Code :",response.status_code)
print(response.json())