import requests

BASE = "http://127.0.0.1:5000"


# =====================================================
# RESTAURANT
# =====================================================

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


# =====================================================
# DISH
# =====================================================

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


# =====================================================
# SEARCH
# =====================================================

def test_10_search():
    r = requests.get(f"{BASE}/api/v1/restaurants/search?name=Pytest")
    assert r.status_code == 200


# =====================================================
# ORDER
# =====================================================

def test_11_place_order():
    data = {"user_id": 1, "restaurant_id": 1}
    r = requests.post(f"{BASE}/api/v1/orders", json=data)
    assert r.status_code == 201


def test_12_orders_by_restaurant():
    r = requests.get(f"{BASE}/api/v1/restaurants/1/orders")
    assert r.status_code == 200


def test_13_orders_by_user():
    r = requests.get(f"{BASE}/api/v1/users/1/orders")
    assert r.status_code == 200


# =====================================================
# RATING
# =====================================================

def test_14_rating():
    data = {"order_id": 1, "rating": 5, "comment": "Good"}
    r = requests.post(f"{BASE}/api/v1/ratings", json=data)
    assert r.status_code == 201


# =====================================================
# ADMIN
# =====================================================

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
