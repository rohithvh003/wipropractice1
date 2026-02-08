from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class Desktops:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # -------- LOCATORS --------
    desktops_tab = (By.LINK_TEXT, "Desktops")
    mac_link = (By.LINK_TEXT, "Mac (1)")
    # mac_heading = (By.NAME, "Mac")

    sort_dropdown = (By.ID, "input-sort")
    add_to_cart_btn = (By.XPATH, "//button[contains(@onclick,'cart.add')]")

    search_box = (By.NAME, "search")
    search_btn = (By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")

    search_criteria = (By.ID, "input-search")
    search_desc_checkbox = (By.NAME, "description")
    search_btn_2 = (By.ID, "button-search")

    # -------- ACTION METHODS --------
    def open_mac_page(self):
        self.driver.find_element(*self.desktops_tab).click()
        self.driver.find_element(*self.mac_link).click()

    # def verify_mac_heading(self):
    #     heading = self.wait.until(
    #         EC.visibility_of_element_located(self.mac_heading)
    #     )
    #     return heading.text == "Mac"

    def sort_name_az(self):
        dropdown = Select(
            self.wait.until(EC.visibility_of_element_located(self.sort_dropdown))
        )
        dropdown.select_by_visible_text("Name (A - Z)")

    def add_first_product_to_cart(self):
        self.driver.find_element(*self.add_to_cart_btn).click()

    def search_product(self, product_name):
        self.wait.until(
            EC.visibility_of_element_located(self.search_box)
        ).clear()
        self.driver.find_element(*self.search_box).send_keys(product_name)
        self.driver.find_element(*self.search_btn).click()

    def advanced_search(self):
        self.wait.until(
            EC.visibility_of_element_located(self.search_criteria)
        ).clear()
        self.driver.find_element(*self.search_desc_checkbox).click()
        self.driver.find_element(*self.search_btn_2).click()
