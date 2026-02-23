import pytest
import random
import string
from datetime import datetime
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://demowebshop.tricentis.com/"


# ---------- FIXTURE ----------
@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()


# ---------- SCREENSHOT ON FAILURE ----------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs["setup"]
        os.makedirs("screenshots", exist_ok=True)
        driver.save_screenshot(
            f"screenshots/fail_{datetime.now().timestamp()}.png"
        )


# ---------- HELPER FUNCTION ----------
def generate_email():
    random_string = ''.join(random.choices(string.ascii_lowercase, k=5))
    return f"auto_{random_string}@test.com"


# ---------- COMPLETE END TO END TEST ----------
def test_complete_ecommerce_flow(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    # ----------------- REGISTER -----------------
    driver.find_element(By.CLASS_NAME, "ico-register").click()

    email = generate_email()

    driver.find_element(By.ID, "gender-male").click()
    driver.find_element(By.ID, "FirstName").send_keys("Akash")
    driver.find_element(By.ID, "LastName").send_keys("Tester")
    driver.find_element(By.ID, "Email").send_keys(email)
    driver.find_element(By.ID, "Password").send_keys("Password123")
    driver.find_element(By.ID, "ConfirmPassword").send_keys("Password123")
    driver.find_element(By.ID, "register-button").click()

    assert "Your registration completed" in driver.page_source

    # ----------------- LOGOUT AFTER REGISTER -----------------
    driver.find_element(By.CLASS_NAME, "ico-logout").click()

    # ----------------- LOGIN -----------------
    driver.find_element(By.CLASS_NAME, "ico-login").click()

    driver.find_element(By.ID, "Email").send_keys(email)
    driver.find_element(By.ID, "Password").send_keys("Password123")
    driver.find_element(By.CSS_SELECTOR, "input.login-button").click()

    assert "My account" in driver.page_source

    # ----------------- SEARCH PRODUCT -----------------
    driver.find_element(By.ID, "small-searchterms").send_keys("laptop")
    driver.find_element(By.CSS_SELECTOR, "input.search-box-button").click()

    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-item h2 a"))
    ).click()

    # ----------------- ADD TO CART -----------------
    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='Add to cart']"))
    ).click()

    # ----------------- OPEN CART -----------------
    driver.find_element(By.CLASS_NAME, "ico-cart").click()

    assert "Shopping cart" in driver.page_source

    # ----------------- REMOVE ITEM -----------------
    driver.find_element(By.NAME, "removefromcart").click()
    driver.find_element(By.NAME, "updatecart").click()

    assert "empty" in driver.page_source.lower()

    # ----------------- LOGOUT -----------------
    driver.find_element(By.CLASS_NAME, "ico-logout").click()

    assert "Log in" in driver.page_source
