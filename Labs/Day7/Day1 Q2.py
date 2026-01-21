from flask import Flask ,request,jsonify

app2 = Flask(__name__)

users = [{"id":1,"name":"Rohith"},
         {"id":2,"name":"Akash"}
         ]
@app2.route("/")
def home():
    return f"Welcome to API"

@app2.route("/users",methods=["GET"])
def get_users():
    return jsonify(users), 200

@app2.route("/users/<int:user_id>",methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"]== user_id:
            return jsonify(user), 200
    return jsonify({"error":"User not found"}), 404


@app2.route("/users",methods=["POST"])
def add_user():
    data=request.json
    newuser={
        "id":len(users)+1,"name":data.get("name")
    }
    users.append(newuser)
    return jsonify(newuser),201

@app2.route("/users/<int:user_id>",methods=["PUT"])
def update_user(user_id):
    data = request.json
    for user in users:
        if user["id"] == user_id:
            user["name"] =data.get("name")
            return jsonify(user)
    return jsonify({"message":"user not found"}),404


if __name__ == '__main__':
    app2.run(debug=True)