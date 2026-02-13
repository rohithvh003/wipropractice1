import sys
from flask import Flask, request, jsonify
import pytest
import requests

# =========================================================
#                   FLASK APP
# =========================================================
app = Flask(__name__)

# in-memory DB
movies = {
    101: {
        "id": 101,
        "movie_name": "Mark",
        "language": "English",
        "duration": "2h 49m",
        "price": 250,
    }
}

# ---------- GET all ----------
@app.get("/api/movies")
def get_movies():
    return jsonify(list(movies.values())), 200


# ---------- GET by id ----------
@app.get("/api/movies/<int:movie_id>")
def get_movie(movie_id):
    movie = movies.get(movie_id)
    if movie:
        return jsonify(movie), 200
    return jsonify({"error": "Movie not found"}), 404


# ---------- ADD ----------
@app.post("/api/movies")
def add_movie():
    data = request.json

    if isinstance(data, list):  # bulk insert
        for movie in data:
            movies[movie["id"]] = movie
        return jsonify({"message": "Bulk insert success"}), 201

    if "id" not in data:
        return jsonify({"error": "Invalid data"}), 400

    movies[data["id"]] = data
    return jsonify(data), 201


# @app.route("/api/movies", methods=["POST"])
# def add_movie():
#     data = request.get_json()
#
#     # check if id is present
#     if "id" not in data:
#         return {"error": "Movie id required"}, 400
#
#     # store movie
#     movies[data["id"]] = data
#
#     return data, 201








# ---------- UPDATE ----------
@app.put("/api/movies/<int:movie_id>")
def update_movie(movie_id):
    if movie_id not in movies:
        return jsonify({"error": "Movie not found"}), 404
    movies[movie_id].update(request.json)
    return jsonify(movies[movie_id]), 200


# ---------- DELETE ----------
@app.delete("/api/movies/<int:movie_id>")
def delete_movie(movie_id):
    if movie_id not in movies:
        return jsonify({"error": "Movie not found"}), 404
    del movies[movie_id]
    return jsonify({"message": "Deleted"}), 200


# ---------- BOOK ----------
@app.post("/api/bookings")
def book_ticket():
    data = request.json
    movie_id = data.get("movie_id")
    seats = data.get("seats", 1)

    if movie_id not in movies:
        return jsonify({"error": "Movie not found"}), 404

    total = seats * movies[movie_id]["price"]
    return jsonify({"message": "Booking confirmed", "total": total}), 201


# =========================================================
#                   PYTEST SECTION
# =========================================================
BASE_URL = "http://127.0.0.1:5000"


@pytest.fixture(scope="module")
def sample_movie():
    return {
        "id": 999,
        "movie_name": "Test Movie",
        "language": "English",
        "duration": "2h",
        "price": 200,
    }


# ---------- FETCH ----------
def test_get_movies():
    r = requests.get(f"{BASE_URL}/api/movies")
    assert r.status_code == 200
    assert isinstance(r.json(), list)


# ---------- ADD ----------
def test_add_movie(sample_movie):
    r = requests.post(f"{BASE_URL}/api/movies", json=sample_movie)
    assert r.status_code == 201
    assert r.json()["id"] == 999


# ---------- PARAMETERIZED GET ----------
@pytest.mark.parametrize("movie_id, status", [(999, 200), (555, 404)])
def test_get_movie_by_id(movie_id, status):
    r = requests.get(f"{BASE_URL}/api/movies/{movie_id}")
    assert r.status_code == status


# ---------- BOOK ----------
def test_booking():
    payload = {"movie_id": 101, "seats": 2}
    r = requests.post(f"{BASE_URL}/api/bookings", json=payload)
    assert r.status_code == 201
    assert "total" in r.json()


# =========================================================
#                   RUN SERVER
# =========================================================
if __name__ == "__main__":
    if "run" in sys.argv:
        app.run(debug=True)
