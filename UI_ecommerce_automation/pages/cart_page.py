from selenium.webdriver.common.by import By
from UI_ecommerce_automation.pages.base_page import BasePage


class CartPage(BasePage):

    CART_LINK = (By.CLASS_NAME, "ico-cart")
    REMOVE = (By.NAME, "removefromcart")
    UPDATE = (By.NAME, "updatecart")
    LOGOUT = (By.CLASS_NAME, "ico-logout")

    def remove_item(self):
        self.click(self.CART_LINK)
        self.click(self.REMOVE)
        self.click(self.UPDATE)

    def logout(self):
        self.click(self.LOGOUT)
