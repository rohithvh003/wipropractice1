from Techademy_Assessment.Day11.Q2.app import login, add_to_cart

def test_successful_login():
    result = login("admin", "admin123")
    assert result == "Login Successful"


def test_failed_login():
    result = login("user", "wrongpass")
    assert result == "Login Failed"


def test_add_item_to_cart():
    result = add_to_cart("Laptop")
    assert result == "Laptop added to cart"


def test_add_empty_item():
    result = add_to_cart("")
    assert result == "No item selected"
