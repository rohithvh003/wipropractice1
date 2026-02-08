from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class Desktops_PageFactory:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ---------- PAGE FACTORY ELEMENTS ----------
    @property
    def desktops_tab(self):
        return self.driver.find_element(By.LINK_TEXT, "Desktops")

    @property
    def mac_link(self):
        return self.driver.find_element(By.LINK_TEXT, "Mac (1)")

    @property
    def sort_dropdown(self):
        return self.driver.find_element(By.ID, "input-sort")

    @property
    def add_to_cart_btn(self):
        return self.driver.find_element(
            By.XPATH, "//button[contains(@onclick,'cart.add')]"
        )

    @property
    def search_box(self):
        return self.driver.find_element(By.NAME, "search")

    @property
    def search_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")

    @property
    def search_desc_checkbox(self):
        return self.driver.find_element(By.NAME, "description")

    @property
    def search_btn_2(self):
        return self.driver.find_element(By.ID, "button-search")

    # ---------- ACTION METHODS ----------
    def open_mac_page(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Desktops")))
        self.desktops_tab.click()

        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Mac (1)")))
        self.mac_link.click()

    def sort_name_az(self):
        # WAIT MUST USE LOCATOR, NOT WebELEMENT
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "input-sort"))
        )

        dropdown = Select(self.sort_dropdown)
        dropdown.select_by_visible_text("Name (A - Z)")

    def add_first_product_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@onclick,'cart.add')]")
            )
        )
        self.add_to_cart_btn.click()

    def search_product(self, product_name):
        self.wait.until(EC.visibility_of_element_located((By.NAME, "search")))
        self.search_box.clear()
        self.search_box.send_keys(product_name)
        self.search_btn.click()

    def advanced_search(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")
            )
        ).click()

        self.search_desc_checkbox.click()
        self.search_btn_2.click()
