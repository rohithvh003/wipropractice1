from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@type='submit']")

    def enter_username(self, user):
        self.wait.until(EC.visibility_of_element_located(self.username)).send_keys(user)

    def enter_password(self, pwd):
        self.driver.find_element(*self.password).send_keys(pwd)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
