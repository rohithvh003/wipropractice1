from selenium.webdriver.common.by import By
from UI_ecommerce_automation.pages.base_page import BasePage


class CartPage(BasePage):
    CART_LINK = (By.CLASS_NAME, "ico-cart")
    REMOVE = (By.NAME, "removefromcart")
    UPDATE = (By.NAME, "updatecart")

    def open_cart(self):
        self.click(self.CART_LINK)

    def remove_item(self):
        self.click(self.REMOVE)
        self.click(self.UPDATE)
