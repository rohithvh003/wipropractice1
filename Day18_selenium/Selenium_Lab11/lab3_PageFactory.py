from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class Desktops_PageFactory:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # -------- PAGE FACTORY ELEMENTS --------
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
        return self.driver.find_element(By.XPATH, "//button[contains(@onclick,'cart.add')]")

    # -------- PAGE ACTION METHODS --------
    def open_mac_page(self):
        self.desktops_tab.click()
        self.mac_link.click()

    def sort_name_az(self):
        dropdown = Select(
            self.wait.until(EC.visibility_of(self.sort_dropdown))
        )
        dropdown.select_by_visible_text("Name (A - Z)")

    def add_first_product_to_cart(self):
        self.add_to_cart_btn.click()
