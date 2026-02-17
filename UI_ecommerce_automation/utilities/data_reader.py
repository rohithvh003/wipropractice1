import json

def get_data():
    with open("data/test_data.json") as f:
        return json.load(f)
