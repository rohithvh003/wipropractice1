from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, wait=10):
        self.driver = driver
        self.wait = wait

    def click(self, locator):
        WebDriverWait(self.driver, self.wait).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def type(self, locator, value):
        WebDriverWait(self.driver, self.wait).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(value)
