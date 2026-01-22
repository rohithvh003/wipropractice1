# 1. Uses the requests library to send a GET request to a public REST API (e.g., users or posts API)

import requests


url = "http://127.0.0.1:5000/users"
response = requests.get(url)
print("status code",response.status_code)
print(response.json)