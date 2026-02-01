def login(username, password):
    if username == "admin" and password == "admin123":
        return "Login Successful"
    return "Login Failed"


def add_to_cart(item):
    if item:
        return f"{item} added to cart"
    return "No item selected"
