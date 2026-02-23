import json

def get_data():
    with open("data/data.csv") as f:
        return json.load(f)
