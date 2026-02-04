import requests

def test_get_all_movies(base_url):
    response = requests.get(f"{base_url}/api/movies")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_movie(base_url):
    payload = {
        "id": 102,
        "movie_name": "Inception",
        "language": "English",
        "duration": "2h 28m",
        "price": 300
    }
    response = requests.post(f"{base_url}/api/movies", json=payload)
    assert response.status_code == 201

def test_book_movie(base_url):
    payload = {
        "movie_id": 102,
        "seats": 2
    }
    response = requests.post(f"{base_url}/api/bookings", json=payload)
    assert response.status_code == 201
    assert response.json()["message"] == "Booking successful"
