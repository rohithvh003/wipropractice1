from flask import Flask, request, jsonify
from storage import read_file, write_file, generate_id

app = Flask(__name__)

print("APP STARTED")

# =====================================================
# RESTAURANT MODULE
# =====================================================

# Register Restaurant
@app.route("/api/v1/restaurants", methods=["POST"])
def add_restaurant():
    data = request.json
    restaurants = read_file("restaurants.json")

    for r in restaurants:
        if r["name"] == data.get("name"):
            return jsonify({"error": "Restaurant exists"}), 409

    new = {
        "id": generate_id(restaurants),
        "name": data.get("name"),
        "category": data.get("category"),
        "location": data.get("location"),
        "contact": data.get("contact"),
        "active": True,
        "approved": False
    }

    restaurants.append(new)
    write_file("restaurants.json", restaurants)

    return jsonify(new), 201


# List Restaurants
@app.route("/api/v1/restaurants", methods=["GET"])
def list_restaurants():
    return jsonify(read_file("restaurants.json")), 200


# View Restaurant Profile
@app.route("/api/v1/restaurants/<int:rid>", methods=["GET"])
def get_restaurant(rid):
    restaurants = read_file("restaurants.json")

    for r in restaurants:
        if r["id"] == rid:
            return jsonify(r), 200

    return jsonify({"error": "Not found"}), 404


# Update Restaurant
@app.route("/api/v1/restaurants/<int:rid>", methods=["PUT"])
def update_restaurant(rid):
    restaurants = read_file("restaurants.json")

    for r in restaurants:
        if r["id"] == rid:
            for k, v in request.json.items():
                r[k] = v
            write_file("restaurants.json", restaurants)
            return jsonify(r), 200

    return jsonify({"error": "Not found"}), 404


# Disable Restaurant
@app.route("/api/v1/restaurants/<int:rid>/disable", methods=["PUT"])
def disable_restaurant(rid):
    restaurants = read_file("restaurants.json")

    for r in restaurants:
        if r["id"] == rid:
            r["active"] = False
            write_file("restaurants.json", restaurants)
            return jsonify({"message": "Restaurant disabled"}), 200

    return jsonify({"error": "Not found"}), 404


# =====================================================
# DISH MODULE
# =====================================================

# Add Dish
@app.route("/api/v1/restaurants/<int:rid>/dishes", methods=["POST"])
def add_dish(rid):
    dishes = read_file("dishes.json")

    new = request.json
    new["id_dishes"] = generate_id(dishes)
    new["restaurant_id"] = rid
    new["enabled"] = True

    dishes.append(new)
    write_file("dishes.json", dishes)

    return jsonify(new), 201


# Update Dish
@app.route("/api/v1/dishes/<int:did>", methods=["PUT"])
def update_dish(did):
    dishes = read_file("dishes.json")

    for d in dishes:
        if d["id"] == did:
            for k, v in request.json.items():
                d[k] = v
            write_file("dishes.json", dishes)
            return jsonify(d), 200

    return jsonify({"error": "Not found"}), 404


# Enable / Disable Dish
@app.route("/api/v1/dishes/<int:did>/status", methods=["PUT"])
def dish_status(did):
    dishes = read_file("dishes.json")

    for d in dishes:
        if d["id"] == did:
            d["enabled"] = request.json.get("enabled")
            write_file("dishes.json", dishes)
            return jsonify({"message": "Status updated"}), 200

    return jsonify({"error": "Not found"}), 404


# Delete Dish
@app.route("/api/v1/dishes/<int:did>", methods=["DELETE"])
def delete_dish(did):
    dishes = read_file("dishes.json")

    for d in dishes:
        if d["id"] == did:
            dishes.remove(d)
            write_file("dishes.json", dishes)
            return jsonify({"message": "Dish deleted"}), 200

    return jsonify({"error": "Not found"}), 404


# =====================================================
# USER MODULE
# =====================================================

# User Registration
@app.route("/api/v1/users/register", methods=["POST"])
def register_user():
    users = read_file("users.json")
    data = request.json

    for u in users:
        if u["email"] == data.get("email"):
            return jsonify({"error": "User exists"}), 409

    data["id"] = generate_id(users)
    users.append(data)
    write_file("users.json", users)

    return jsonify(data), 201


# =====================================================
# SEARCH MODULE
# =====================================================

@app.route("/api/v1/restaurants/search", methods=["GET"])
def search_restaurant():
    name = request.args.get("name")
    location = request.args.get("location")

    restaurants = read_file("restaurants.json")
    result = []

    for r in restaurants:
        if name and name.lower() not in r["name"].lower():
            continue
        if location and location.lower() not in r["location"].lower():
            continue
        result.append(r)

    return jsonify(result), 200


# =====================================================
# ORDER MODULE
# =====================================================

# Place Order
@app.route("/api/v1/orders", methods=["POST"])
def place_order():
    orders = read_file("orders.json")
    data = request.json

    data["id_orders"] = generate_id(orders)
    orders.append(data)
    write_file("orders.json", orders)

    return jsonify(data), 201


# Orders by Restaurant
@app.route("/api/v1/restaurants/<int:rid>/orders", methods=["GET"])
def orders_by_restaurant(rid):
    orders = read_file("orders.json")
    result = [o for o in orders if o["restaurant_id"] == rid]
    return jsonify(result), 200


# Orders by User
@app.route("/api/v1/users/<int:uid>/orders", methods=["GET"])
def orders_by_user(uid):
    orders = read_file("orders.json")
    result = [o for o in orders if o["user_id"] == uid]
    return jsonify(result), 200


# =====================================================
# RATINGS / FEEDBACK
# =====================================================

@app.route("/api/v1/ratings", methods=["POST"])
def give_rating():
    ratings = read_file("ratings.json")
    data = request.json

    data["id"] = generate_id(ratings)
    ratings.append(data)
    write_file("ratings.json", ratings)

    return jsonify(data), 201


# =====================================================
# ADMIN MODULE
# =====================================================

# Approve Restaurant
@app.route("/api/v1/admin/restaurants/<int:rid>/approve", methods=["PUT"])
def approve_restaurant(rid):
    restaurants = read_file("restaurants.json")

    for r in restaurants:
        if r["id"] == rid:
            r["approved"] = True
            write_file("restaurants.json", restaurants)
            return jsonify({"message": "Approved"}), 200

    return jsonify({"error": "Not found"}), 404


# Admin Disable Restaurant
@app.route("/api/v1/admin/restaurants/<int:rid>/disable", methods=["PUT"])
def admin_disable(rid):
    restaurants = read_file("restaurants.json")

    for r in restaurants:
        if r["id"] == rid:
            r["active"] = False
            write_file("restaurants.json", restaurants)
            return jsonify({"message": "Disabled"}), 200

    return jsonify({"error": "Not found"}), 404


# View Feedback
@app.route("/api/v1/admin/feedback", methods=["GET"])
def admin_feedback():
    return jsonify(read_file("ratings.json")), 200


# View All Orders
@app.route("/api/v1/admin/orders", methods=["GET"])
def admin_orders():
    return jsonify(read_file("orders.json")), 200


# =====================================================
# RUN SERVER
# =====================================================

if __name__ == "__main__":
    app.run(debug=True)
