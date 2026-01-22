import requests

BASE_URL = "http://127.0.0.1:5000"

headers = {
    "Accept": "application/json",
    "User-Agent": "Python-Request-Client"
}

# GET
response = requests.get(f"{BASE_URL}/users", headers=headers)
print("GET:", response.status_code, response.json())

# POST
response = requests.post(
    f"{BASE_URL}/users",
    json={"name": "rohith"},
    headers=headers
)
print("POST:", response.status_code, response.json())

# PUT
response = requests.put(
    f"{BASE_URL}/users/2",
    json={"name": "vijay"},
    headers=headers
)
print("PUT:", response.status_code, response.json())

# PATCH
response = requests.patch(
    f"{BASE_URL}/users/1",
    json={"name": "Raju Updated"},
    headers=headers
)
print("PATCH:", response.status_code, response.json())

# DELETE
response = requests.delete(f"{BASE_URL}/users/2", headers=headers)
print("DELETE:", response.status_code, response.json())
