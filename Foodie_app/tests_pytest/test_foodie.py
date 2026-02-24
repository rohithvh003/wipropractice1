import requests
import time

BASE = "http://127.0.0.1:5000"



def test_01_register_restaurant():
    data = {
        "name": "Pytest Hotel",
        "category": "Indian",
        "location": "Chennai",
        "contact": "999"
    }
    r = requests.post(f"{BASE}/api/v1/restaurants", json=data)
    assert r.status_code in [201, 409]


def test_02_view_restaurant():
    r = requests.get(f"{BASE}/api/v1/restaurants/1")
    assert r.status_code in [200, 404]


def test_03_update_restaurant():
    r = requests.put(f"{BASE}/api/v1/restaurants/1", json={"location": "Delhi"})
    assert r.status_code in [200, 404]


def test_04_disable_restaurant():
    r = requests.put(f"{BASE}/api/v1/restaurants/1/disable")
    assert r.status_code in [200, 404]


def test_05_add_dish():
    data = {"name": "Burger", "type": "veg", "price": 120}
    r = requests.post(f"{BASE}/api/v1/restaurants/1/dishes", json=data)
    assert r.status_code == 201


def test_06_update_dish():
    r = requests.put(f"{BASE}/api/v1/dishes/1", json={"price": 150})
    assert r.status_code in [200, 404]


def test_07_dish_status():
    r = requests.put(f"{BASE}/api/v1/dishes/1/status", json={"enabled": False})
    assert r.status_code in [200, 404]


def test_08_delete_dish():
    r = requests.delete(f"{BASE}/api/v1/dishes/1")
    assert r.status_code in [200, 404]


# =====================================================
# USER
# =====================================================

def test_09_register_user():
    data = {"name": "Py User", "email": "py@mail.com", "password": "123"}
    r = requests.post(f"{BASE}/api/v1/users/register", json=data)
    assert r.status_code in [201, 409]

def test_10_search():
    r = requests.get(f"{BASE}/api/v1/restaurants/search?name=Pytest")
    assert r.status_code == 200


def test_place_order():

    # ----------------------------
    # Create Unique Restaurant
    # ----------------------------
    unique_restaurant = f"TestHotel_{int(time.time())}"

    r = requests.post(f"{BASE}/api/v1/restaurants", json={
        "name": unique_restaurant,
        "category": "Indian"
    })

    print("Create Restaurant:", r.status_code, r.json())
    assert r.status_code == 201, "Restaurant creation failed"

    restaurant_data = r.json()
    assert "id" in restaurant_data
    rid = restaurant_data["id"]

    # ----------------------------
    # Approve Restaurant
    # ----------------------------
    approve = requests.put(
        f"{BASE}/api/v1/admin/restaurants/{rid}/approve"
    )

    print("Approve Restaurant:", approve.status_code)
    assert approve.status_code == 200, "Restaurant approval failed"

    # ----------------------------
    # Add Dish
    # ----------------------------
    dish = requests.post(
        f"{BASE}/api/v1/restaurants/{rid}/dishes",
        json={"name": "Pizza", "price": 200}
    )

    print("Add Dish:", dish.status_code)
    assert dish.status_code == 201, "Dish creation failed"

    # ----------------------------
    # Create Unique User
    # ----------------------------
    unique_email = f"user_{int(time.time())}@mail.com"

    u = requests.post(
        f"{BASE}/api/v1/users/register",
        json={
            "name": "User",
            "email": unique_email,
            "password": "123"
        }
    )

    print("Create User:", u.status_code, u.json())
    assert u.status_code == 201, "User creation failed"

    user_data = u.json()
    assert "id" in user_data
    uid = user_data["id"]

    # ----------------------------
    # Place Order
    # ----------------------------
    order = requests.post(
        f"{BASE}/api/v1/orders",
        json={
            "user_id": uid,
            "restaurant_id": rid,
            "items": [
                {"name": "Pizza", "qty": 2}
            ]
        }
    )

    print("Place Order:", order.status_code, order.json())
    assert order.status_code == 201, "Order placement failed"

def test_12_orders_by_restaurant():
    r = requests.get(f"{BASE}/api/v1/restaurants/1/orders")
    assert r.status_code == 200


def test_13_orders_by_user():
    r = requests.get(f"{BASE}/api/v1/users/1/orders")
    assert r.status_code == 200


def test_14_rating():
    data = {"order_id": 1, "rating": 5, "comment": "Good"}
    r = requests.post(f"{BASE}/api/v1/ratings", json=data)
    assert r.status_code == 201




def test_15_admin_approve():
    r = requests.put(f"{BASE}/api/v1/admin/restaurants/1/approve")
    assert r.status_code in [200, 404]


def test_16_admin_disable():
    r = requests.put(f"{BASE}/api/v1/admin/restaurants/1/disable")
    assert r.status_code in [200, 404]


def test_17_admin_feedback():
    r = requests.get(f"{BASE}/api/v1/admin/feedback")
    assert r.status_code == 200


def test_18_admin_orders():
    r = requests.get(f"{BASE}/api/v1/admin/orders")
    assert r.status_code == 200
