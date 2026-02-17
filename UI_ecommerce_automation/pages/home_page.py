from selenium.webdriver.common.by import By
from  UI_ecommerce_automation.pages.base_page import BasePage


class HomePage(BasePage):
    LOGIN_LINK = (By.CLASS_NAME, "ico-login")
    LOGOUT_LINK = (By.CLASS_NAME, "ico-logout")
    SEARCH_BOX = (By.ID, "small-searchterms")
    SEARCH_BTN = (By.CSS_SELECTOR, "input.search-box-button")

    def open_login(self):
        self.click(self.LOGIN_LINK)

    def logout(self):
        self.click(self.LOGOUT_LINK)

    def search(self, product):
        self.type(self.SEARCH_BOX, product)
        self.click(self.SEARCH_BTN)
