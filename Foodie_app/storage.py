import json
import os

BASE = "data"

def read_file(filename):
    path = os.path.join(BASE, filename)
    with open(path, "r") as f:
        return json.load(f)

def write_file(filename, data):
    path = os.path.join(BASE, filename)
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def generate_id(items):
    if not items:
        return 1
    return max(item["id"] for item in items) + 1
