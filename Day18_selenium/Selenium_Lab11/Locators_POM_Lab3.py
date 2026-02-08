from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Desktops:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    desktops_tab = (By.LINK_TEXT, "Desktops")

    mac_link = (By.LINK_TEXT,"Mac (1)")
    sort_dropdown = (By.ID, "input-sort")
    add_to_cart_btn = (By.XPATH, "//button[contains(@onclick,'cart.add')]")

    def open_mac_page(self):
        self.driver.find_element(*self.desktops_tab).click()
        self.driver.find_element(*self.mac_link).click()

    def sort_name_az(self):
        dropdown = Select(
            self.wait.until(EC.visibility_of_element_located(self.sort_dropdown))
        )
        dropdown.select_by_visible_text("Name (A - Z)")

    def add_first_product_to_cart(self):
        self.driver.find_element(*self.add_to_cart_btn).click()