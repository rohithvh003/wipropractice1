# 5. Handles HTTP errors using proper exception handling


import requests

url = "http://127.0.0.1:5000/users"

try:
    response = requests.get(url)
    response.raise_for_status()
    print(response.json())

except requests.exceptions.HTTPError:
    print("HTTP error occurred")

except requests.exceptions.RequestException:
    print("Request failed")

except Exception:
    print("Unexpected error occurred")
