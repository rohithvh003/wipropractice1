from selenium.webdriver.common.by import By
from UI_ecommerce_automation.pages.base_page import BasePage


class RegisterPage(BasePage):
    REGISTER_LINK = (By.CLASS_NAME, "ico-register")

    GENDER = (By.ID, "gender-male")
    FIRSTNAME = (By.ID, "FirstName")
    LASTNAME = (By.ID, "LastName")
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    CONFIRM_PASSWORD = (By.ID, "ConfirmPassword")
    REGISTER_BTN = (By.ID, "register-button")

    def open_register(self):
        self.click(self.REGISTER_LINK)

    def register_user(self, data):
        self.click(self.GENDER)
        self.type(self.FIRSTNAME, data["first_name"])
        self.type(self.LASTNAME, data["last_name"])
        self.type(self.EMAIL, data["email"])
        self.type(self.PASSWORD, data["password"])
        self.type(self.CONFIRM_PASSWORD, data["password"])
        self.click(self.REGISTER_BTN)
