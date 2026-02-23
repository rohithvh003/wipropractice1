from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from UI_Ecommerce_Project.pages.base_page import BasePage


class ProductPage(BasePage):

    add_to_cart_button = (By.XPATH, "//input[@value='Add to cart']")
    success_bar = (By.CSS_SELECTOR, ".bar-notification.success")

    def add_to_cart(self):
        self.click(self.add_to_cart_button)

    def wait_for_success_message(self):
        self.wait.until(
            EC.text_to_be_present_in_element(
                self.success_bar,
                "The product has been added"
            )
        )
        return True
