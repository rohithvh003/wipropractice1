from UI_ecommerce_automation.pages.home_page import HomePage
from UI_ecommerce_automation.pages.product_page import ProductPage
from UI_ecommerce_automation.pages.cart_page import CartPage
from UI_ecommerce_automation.utilities.data_reader import get_data


def test_cart_flow(setup):
    driver = setup
    data = get_data()

    home = HomePage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)

    home.search(data["product"]["name"])
    product.open_first_product()
    product.add_to_cart()

    cart.open_cart()
    cart.remove_item()

    assert "empty" in driver.page_source.lower()
