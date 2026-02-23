from selenium.webdriver.common.by import By
from UI_Ecommerce_Project.pages.base_page import BasePage


class LoginPage(BasePage):

    email = (By.ID, "Email")
    password = (By.ID, "Password")
    login_button = (By.XPATH, "//input[@value='Log in']")

    def login(self, email_value, password_value):
        self.send_keys(self.email, email_value)
        self.send_keys(self.password, password_value)
        self.click(self.login_button)
