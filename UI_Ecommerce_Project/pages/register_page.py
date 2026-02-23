from selenium.webdriver.common.by import By
from UI_Ecommerce_Project.pages.base_page import BasePage


class RegisterPage(BasePage):

    gender_male = (By.ID, "gender-male")
    first_name = (By.ID, "FirstName")
    last_name = (By.ID, "LastName")
    email = (By.ID, "Email")
    password = (By.ID, "Password")
    confirm_password = (By.ID, "ConfirmPassword")
    register_button = (By.ID, "register-button")

    def register(self, user):
        self.click(self.gender_male)
        self.send_keys(self.first_name, user["first_name"])
        self.send_keys(self.last_name, user["last_name"])
        self.send_keys(self.email, user["email"])
        self.send_keys(self.password, user["password"])
        self.send_keys(self.confirm_password, user["password"])
        self.click(self.register_button)
