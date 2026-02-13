import sys
from flask import Flask, jsonify, request

app = Flask(__name__)

movies = {101:{
    "id": 101,
    "title": "Movie",
    "language": "Python",
    "genre": "Action",
}}

@app.get("/api/movies")
def get_movies(movies):
    return jsonify(list(movies.values()))

@app.get("/api/movies/<int:movies_id")
def get_movie(movie_id):
    movie = movies.get(movie_id)
    if movie:
        return jsonify(movie), 200
    return jsonify({"message": "Movie not found"}), 404

@app.post("/api/movies/<int:movie_id>")
def add_movie(id):
    data = request.get_json()
    if id not in data:
        return jsonify({"message": "Movie not found"}), 404
    movies[data["id"]] = data
    return data, 201

@app.put("/api/movies/<int:movie_id>")
def update_movie(movie_id):
    if movie_id not in movies:
        return jsonify({"message": "Movie not found"}), 404
    movies[movie_id]["id"]] = request.json
