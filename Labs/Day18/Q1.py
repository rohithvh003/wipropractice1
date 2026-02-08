from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ---------- BASE PAGE (reusable methods) ----------
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        time.sleep(1)

    def type(self, locator, text):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        time.sleep(1)
        el.send_keys(text)
        time.sleep(2)


# ---------- Page Class (POM) ----------
class HomePage(BasePage):
    search_box = (By.NAME, "search")
    search_btn = (By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")

    def search_product(self, name):
        self.type(self.search_box, name)
        self.click(self.search_btn)


# ---------- Test (pytest) ----------
def test_search_product():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(2)

    page = HomePage(driver)
    page.search_product("MacBook")

    print(" Test executed successfully")

    time.sleep(2)
    driver.quit()
