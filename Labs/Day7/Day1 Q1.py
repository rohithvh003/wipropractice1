from flask import Flask ,request,jsonify

app1 = Flask(__name__)

users = [{"id":1,"name":"Rohith"},
         {"id":2,"name":"Akash"}
         ]
@app1.route("/")
def home():
    return f"Welcome to API"

@app1.route("/users",methods=["GET"])
def get_users():
    return jsonify(users), 200

@app1.route("/users/<int:user_id>",methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"]== user_id:
            return jsonify(user), 200
    return jsonify({"error":"User not found"}), 404


@app1.route("/users",methods=["POST"])
def add_user():
    data=request.json
    newuser={
        "id":len(users)+1,"name":data.get("name")
    }
    users.append(newuser)
    return jsonify(newuser),201




if __name__ == '__main__':
    app1.run(debug=True)