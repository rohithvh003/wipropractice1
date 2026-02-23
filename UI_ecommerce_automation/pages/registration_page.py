import random
import string
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

    def generate_email(self):
        random_string = ''.join(random.choices(string.ascii_lowercase, k=5))
        return f"auto_{random_string}@test.com"

    def register_user(self, password):
        self.click(self.REGISTER_LINK)

        email = self.generate_email()

        self.click(self.GENDER)
        self.type(self.FIRSTNAME, "Rohith")
        self.type(self.LASTNAME, "v h")
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.type(self.CONFIRM_PASSWORD, password)
        self.click(self.REGISTER_BTN)

        return email
