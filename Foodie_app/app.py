from flask import Flask, request, jsonify
from storage import read_file, write_file, generate_id

app = Flask(__name__)

print("APP STARTED")

def get_restaurant_name(rid):
    restaurants = read_file("restaurants.json")
    for r in restaurants:
        if r.get("id") == rid:
            return r.get("name")
    return None


def get_user_name(uid):
    users = read_file("users.json")
    for u in users:
        if u.get("id") == uid:
            return u.get("name")
    return None

# Restaurant Module


@app.route("/api/v1/restaurants", methods=["POST"])
def add_restaurant():
    data = request.json or {}
    restaurants = read_file("restaurants.json")

    for r in restaurants:
        if r.get("name") == data.get("name"):
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


@app.route("/api/v1/restaurants", methods=["GET"])
def list_restaurants():
    return jsonify(read_file("restaurants.json")), 200


@app.route("/api/v1/restaurants/<int:rid>", methods=["GET"])
def get_restaurant(rid):
    restaurants = read_file("restaurants.json")
    for r in restaurants:
        if r.get("id") == rid:
            return jsonify(r), 200
    return jsonify({"error": "Not found"}), 404


@app.route("/api/v1/restaurants/<int:rid>", methods=["PUT"])
def update_restaurant(rid):
    restaurants = read_file("restaurants.json")

    for r in restaurants:
        if r.get("id") == rid:
            for k, v in (request.json or {}).items():
                r[k] = v
            write_file("restaurants.json", restaurants)
            return jsonify(r), 200

    return jsonify({"error": "Not found"}), 404


@app.route("/api/v1/restaurants/<int:rid>/disable", methods=["PUT"])
def disable_restaurant(rid):
    restaurants = read_file("restaurants.json")

    for r in restaurants:
        if r.get("id") == rid:
            r["active"] = False
            write_file("restaurants.json", restaurants)
            return jsonify({"message": "Restaurant disabled"}), 200

    return jsonify({"error": "Not found"}), 404

# Dish Module


@app.route("/api/v1/restaurants/<int:rid>/dishes", methods=["POST"])
def add_dish(rid):
    dishes = read_file("dishes.json")
    data = request.json or {}

    if not data.get("name") or not data.get("price"):
        return jsonify({"error": "Missing fields"}), 400

    new = {
        "id_dishes": generate_id(dishes, "id_dishes"),
        "name": data["name"],
        "type": data.get("type", "veg"),
        "price": data["price"],
        "restaurant_id": rid,
        "enabled": True
    }

    dishes.append(new)
    write_file("dishes.json", dishes)

    return jsonify(new), 201


@app.route("/api/v1/dishes", methods=["GET"])
def list_dishes():
    return jsonify(read_file("dishes.json")), 200


@app.route("/api/v1/dishes/<int:did>", methods=["PUT"])
def update_dish(did):
    dishes = read_file("dishes.json")

    for d in dishes:
        if d.get("id_dishes") == did:
            for k, v in (request.json or {}).items():
                d[k] = v
            write_file("dishes.json", dishes)
            return jsonify(d), 200

    return jsonify({"error": "Not found"}), 404


@app.route("/api/v1/dishes/<int:did>/status", methods=["PUT"])
def dish_status(did):
    dishes = read_file("dishes.json")

    for d in dishes:
        if d.get("id_dishes") == did:
            d["enabled"] = request.json.get("enabled")
            write_file("dishes.json", dishes)
            return jsonify({"message": "Status updated"}), 200

    return jsonify({"error": "Not found"}), 404


@app.route("/api/v1/dishes/<int:did>", methods=["DELETE"])
def delete_dish(did):
    dishes = read_file("dishes.json")

    for d in dishes:
        if d.get("id_dishes") == did:
            dishes.remove(d)
            write_file("dishes.json", dishes)
            return jsonify({"message": "Dish deleted"}), 200

    return jsonify({"error": "Not found"}), 404

# User Module

@app.route("/api/v1/users/register", methods=["POST"])
def register_user():
    users = read_file("users.json")
    data = request.json or {}

    for u in users:
        if u.get("email") == data.get("email"):
            return jsonify({"error": "User exists"}), 409

    new = {
        "id": generate_id(users),
        "name": data.get("name"),
        "email": data.get("email"),
        "password": data.get("password")
    }

    users.append(new)
    write_file("users.json", users)

    return jsonify(new), 201


@app.route("/api/v1/users", methods=["GET"])
def list_users():
    return jsonify(read_file("users.json")), 200


@app.route("/api/v1/users/<int:uid>", methods=["GET"])
def get_user(uid):
    users = read_file("users.json")
    for u in users:
        if u.get("id") == uid:
            return jsonify(u), 200
    return jsonify({"error": "User not found"}), 404

# Search


@app.route("/api/v1/restaurants/search", methods=["GET"])
def search_restaurant():
    name = request.args.get("name")
    location = request.args.get("location")

    restaurants = read_file("restaurants.json")
    result = []

    for r in restaurants:
        if name and name.lower() not in (r.get("name") or "").lower():
            continue
        if location and location.lower() not in (r.get("location") or "").lower():
            continue
        result.append(r)

    return jsonify(result), 200

# order module

@app.route("/api/v1/orders", methods=["POST"])
def place_order():
    orders = read_file("orders.json")
    dishes = read_file("dishes.json")
    data = request.json or {}

    user_id = data.get("user_id")
    restaurant_id = data.get("restaurant_id")
    items = data.get("items", [])

    if not items:
        return jsonify({"error": "No items provided"}), 400

    final_items = []
    total = 0

    for item in items:
        name = item.get("name")

        try:
            qty = int(item.get("qty", 1))
        except:
            return jsonify({"error": "Invalid quantity"}), 400

        dish = next(
            (d for d in dishes
             if d.get("name") == name
             and d.get("restaurant_id") == restaurant_id
             and d.get("enabled") == True),
            None
        )

        if not dish:
            return jsonify({"error": f"{name} not available"}), 400


        try:
            price = int(dish.get("price", 0))
        except:
            return jsonify({"error": "Invalid price"}), 500

        total += price * qty

        final_items.append({
            "name": name,
            "qty": qty,
            "price": price
        })

    new_order = {
        "id": generate_id(orders),
        "user_id": user_id,
        "restaurant_id": restaurant_id,
        "items": final_items,
        "total": total
    }

    orders.append(new_order)
    write_file("orders.json", orders)

    response = {
        "id": new_order["id"],
        "user": get_user_name(user_id),
        "restaurant": get_restaurant_name(restaurant_id),
        "items": final_items,
        "total": total
    }

    return jsonify(response), 201



@app.route("/api/v1/restaurants/<int:rid>/orders", methods=["GET"])
def orders_by_restaurant(rid):
    orders = read_file("orders.json")
    result = []

    for o in orders:
        if o.get("restaurant_id") == rid:
            result.append({
                "id": o["id"],
                "user": get_user_name(o["user_id"]),
                "items": o["items"],
                "total": o["total"]
            })

    return jsonify(result), 200


@app.route("/api/v1/users/<int:uid>/orders", methods=["GET"])
def orders_by_user(uid):
    orders = read_file("orders.json")
    result = []

    for o in orders:
        if o.get("user_id") == uid:
            result.append({
                "id": o["id"],
                "restaurant": get_restaurant_name(o["restaurant_id"]),
                "items": o["items"],
                "total": o["total"]
            })

    return jsonify(result), 200
# Rating

@app.route("/api/v1/ratings", methods=["POST"])
def give_rating():
    ratings = read_file("ratings.json")
    data = request.json or {}

    data["id"] = generate_id(ratings)
    ratings.append(data)
    write_file("ratings.json", ratings)

    return jsonify(data), 201

# Admin

@app.route("/api/v1/admin/restaurants/<int:rid>/approve", methods=["PUT"])
def approve_restaurant(rid):
    restaurants = read_file("restaurants.json")

    for r in restaurants:
        if r.get("id") == rid:
            r["approved"] = True
            write_file("restaurants.json", restaurants)
            return jsonify({"message": "Approved"}), 200

    return jsonify({"error": "Not found"}), 404


@app.route("/api/v1/admin/restaurants/<int:rid>/disable", methods=["PUT"])
def admin_disable(rid):
    restaurants = read_file("restaurants.json")

    for r in restaurants:
        if r.get("id") == rid:
            r["active"] = False
            write_file("restaurants.json", restaurants)
            return jsonify({"message": "Disabled"}), 200

    return jsonify({"error": "Not found"}), 404


@app.route("/api/v1/admin/feedback", methods=["GET"])
def admin_feedback():
    return jsonify(read_file("ratings.json")), 200


@app.route("/api/v1/admin/orders", methods=["GET"])
def admin_orders():
    return jsonify(read_file("orders.json")), 200

if __name__ == "__main__":
    app.run(debug=True)
