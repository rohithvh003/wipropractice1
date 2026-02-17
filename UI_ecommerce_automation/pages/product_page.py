from selenium.webdriver.common.by import By
from UI_ecommerce_automation.pages.base_page import BasePage


class ProductPage(BasePage):
    FIRST_PRODUCT = (By.CSS_SELECTOR, ".product-item h2 a")
    ADD_TO_CART = (By.CSS_SELECTOR, "input[value='Add to cart']")

    def open_first_product(self):
        self.click(self.FIRST_PRODUCT)

    def add_to_cart(self):
        self.click(self.ADD_TO_CART)
