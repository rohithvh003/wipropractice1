from selenium.webdriver.common.by import By
from UI_Ecommerce_Project.pages.base_page import BasePage


class SearchPage(BasePage):

    # Locators
    search_box = (By.ID, "small-searchterms")
    search_button = (By.CSS_SELECTOR, "input.button-1.search-box-button")
    first_product = (By.CSS_SELECTOR, ".product-title a")

    # Actions
    def search(self, product_name):
        self.send_keys(self.search_box, product_name)
        self.click(self.search_button)

    def open_first_product(self):
        self.click(self.first_product)
