import logging
import time
import pytest
from selenium.webdriver.common.by import By

from UI_Ecommerce_Project.pages.register_page import RegisterPage
from UI_Ecommerce_Project.pages.login_page import LoginPage
from UI_Ecommerce_Project.pages.search_page import SearchPage
from UI_Ecommerce_Project.pages.product_page import ProductPage
from UI_Ecommerce_Project.Utilities.csv_reader import get_users_from_csv


logger = logging.getLogger(__name__)


@pytest.mark.parametrize("user", get_users_from_csv())
def test_complete_flow(driver, user, base_url):

    # ===== Generate Dynamic Email =====
    unique_email = f"{user['first_name']}_{int(time.time())}@mail.com"
    user["email"] = unique_email

    logger.info(f"Starting test for user: {user['first_name']}")

    # ================= REGISTER =================
    register_page = RegisterPage(driver)
    register_page.open(base_url + "register")
    register_page.register(user)

    logger.info("User registered successfully")

    # ================= LOGIN =================
    login_page = LoginPage(driver)
    login_page.open(base_url + "login")
    login_page.login(user["email"], user["password"])

    assert login_page.is_login_successful(), "Login Failed"
    logger.info("User logged in successfully")

    # ================= SEARCH PRODUCT =================
    search_page = SearchPage(driver)
    search_page.open(base_url)
    search_page.search(user["product"])
    search_page.open_first_product()

    logger.info(f"User searched product: {user['product']}")

    # ================= ADD TO CART =================
    product_page = ProductPage(driver)
    product_page.add_to_cart()
    product_page.wait_for_success_message()

    logger.info("Product added to cart")

    # ================= LOGOUT =================
    driver.find_element(By.LINK_TEXT, "Log out").click()

    logger.info("User logged out successfully")