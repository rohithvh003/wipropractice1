from selenium.webdriver.common.by import By
from UI_ecommerce_automation.pages.base_page import BasePage


class ProductPage(BasePage):

    SEARCH_BOX = (By.ID, "small-searchterms")
    SEARCH_BTN = (By.CSS_SELECTOR, "input.search-box-button")
    FIRST_PRODUCT = (By.CSS_SELECTOR, ".product-item h2 a")
    ADD_TO_CART = (By.CSS_SELECTOR, "input[value='Add to cart']")

    def search_and_add(self, product):
        self.type(self.SEARCH_BOX, product)
        self.click(self.SEARCH_BTN)
        self.click(self.FIRST_PRODUCT)
        self.click(self.ADD_TO_CART)
