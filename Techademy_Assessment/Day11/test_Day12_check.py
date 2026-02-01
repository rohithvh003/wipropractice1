def checkout(total, discount):
    return total - discount

def test_checkout_flow():
    result = checkout(100, 20)
    assert result == 80
