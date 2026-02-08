import requests
import pytest

def test_add_patient(base_url):
    payload = {
        "name": "Akash",
        "age": 22,
        "gender": "Male",
        "contact": "9999999999",
        "disease": "Fever",
        "doctor": "Dr. Smith"
    }
    r = requests.post(base_url, json=payload)
    assert r.status_code == 201
    assert r.json()["name"] == "Akash"

def test_get_patients(base_url):
    r = requests.get(base_url)
    assert r.status_code == 200
    assert isinstance(r.json(), list)

@pytest.mark.parametrize("age", [-1, None])
def test_invalid_patient(base_url, age):
    payload = {
        "name": "Test",
        "age": age
    }
    r = requests.post(base_url, json=payload)
    assert r.status_code == 400
