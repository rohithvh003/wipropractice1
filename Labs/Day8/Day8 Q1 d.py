import json

data = [
    {"id": 1, "name": "Raja"},
    {"id": 2, "name": "Rama"}
]

with open("users.json", "w") as file:
    json.dump(data, file, indent=4)

print("Data saved to JSON file")
