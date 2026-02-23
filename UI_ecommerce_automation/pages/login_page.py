from selenium.webdriver.common.by import By
from UI_ecommerce_automation.pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_LINK = (By.CLASS_NAME, "ico-login")
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    LOGIN_BTN = (By.CSS_SELECTOR, "input.login-button")

    def login(self, email, password):
        self.click(self.LOGIN_LINK)
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)
