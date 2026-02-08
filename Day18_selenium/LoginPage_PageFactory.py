from selenium.webdriver.common.by import By

class Loginpage_PageFactory:
    def __init__(self, driver):
        self.driver = driver

    # -------- PAGE FACTORY STYLE PROPERTIES --------
    @property
    def username(self):
        return self.driver.find_element(By.NAME, "username")

    @property
    def password(self):
        return self.driver.find_element(By.NAME, "password")

    @property
    def click_login(self):
        return self.driver.find_element(By.XPATH, "//button[@type='submit']")

    # -------- ACTION METHODS (FIXED) --------
    def username(self, user):
        self.driver.find_element(By.NAME, "username").send_keys(user)

    def password(self, password):
        self.driver.find_element(By.NAME, "password").send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
