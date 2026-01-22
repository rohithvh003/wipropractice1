# 3. Parses the JSON response and extracts specific fields

import requests


url="http://127.0.0.1:5000/users"

response = requests.get(url)
users = response.json()

for user in users:
    print("Name:",user["name"])
    print("ID:",user["id"])
