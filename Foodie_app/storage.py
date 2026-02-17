import json
import os

BASE = "data"


def read_file(filename):
    path = os.path.join(BASE, filename)
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        try:
            return json.load(f)
        except:
            return []


def write_file(filename, data):
    path = os.path.join(BASE, filename)
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


# UNIVERSAL ID GENERATOR
def generate_id(data, key="id"):
    if not data:
        return 1
    return max(item.get(key, 0) for item in data) + 1
