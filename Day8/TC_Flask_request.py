import requests


geturl ="http://127.0.0.1:5000/users"



response = requests.get(geturl)
print("get status code", response.status_code)
print(response.json())

posturl = "http://127.0.0.1:5000/users"
data = {

    "name": "rohith"
}
response = requests.post(posturl,json=data)
print("post status code", response.status_code)
print(response.json())

puturl = "http://127.0.0.1:5000/users/2"
data ={

    "name":'vijay'
}
response = requests.put(puturl,json=data)
print("put status code", response.status_code)
print(response.json())

patch_url = "http://127.0.0.1:5000/users/1"

data = {
    "name": "Raju Updated"
}

response = requests.patch(patch_url, json=data)
print(response.status_code)
print(response.json())


deleteurl = "http://127.0.0.1:5000/users/2"

response = requests.delete(deleteurl)
print("put status code", response.status_code)
print(response.json())