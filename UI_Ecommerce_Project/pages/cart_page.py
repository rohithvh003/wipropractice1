from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    cart_link = (By.CLASS_NAME, "cart-label")

    def open_cart(self):
        self.click(self.cart_link)
