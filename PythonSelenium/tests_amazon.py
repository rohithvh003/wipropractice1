import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://demowebshop.tricentis.com/"


# ======================================================
# FIXTURE
# ======================================================
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()


# ======================================================
# TEST
# ======================================================
def test_full_ecommerce_flow(driver):
    wait = WebDriverWait(driver, 20)

    # ==================================================
    # 1️⃣ REGISTER
    # ==================================================
    driver.find_element(By.LINK_TEXT, "Register").click()

    wait.until(EC.element_to_be_clickable((By.ID, "gender-male"))).click()

    email = f"test{int(time.time())}@mail.com"

    driver.find_element(By.ID, "FirstName").send_keys("Test")
    driver.find_element(By.ID, "LastName").send_keys("User")
    driver.find_element(By.ID, "Email").send_keys(email)
    driver.find_element(By.ID, "Password").send_keys("Test@123")
    driver.find_element(By.ID, "ConfirmPassword").send_keys("Test@123")

    driver.find_element(By.ID, "register-button").click()

    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "result")))
    print("✅ Registration successful")

    # Continue (if exists)
    try:
        cont = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "input.button-1.register-continue-button")
            )
        )
        cont.click()
    except:
        print("ℹ Continue button skipped")

    # ==================================================
    # 2️⃣ LOGIN (already logged after register, but good practice)
    # ==================================================
    driver.find_element(By.LINK_TEXT, "Log out").click()
    print("✅ Logged out after registration")

    driver.find_element(By.LINK_TEXT, "Log in").click()

    wait.until(EC.visibility_of_element_located((By.ID, "Email"))).send_keys(email)
    driver.find_element(By.ID, "Password").send_keys("Test@123")
    driver.find_element(By.CSS_SELECTOR, "input.login-button").click()

    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log out")))
    print("✅ Login successful")

    # ==================================================
    # 3️⃣ SEARCH PRODUCT
    # ==================================================
    search = wait.until(
        EC.element_to_be_clickable((By.ID, "small-searchterms"))
    )
    search.send_keys("computer")

    driver.find_element(By.CSS_SELECTOR, "input.search-box-button").click()

    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-item"))
    )
    print("✅ Search successful")

    # ==================================================
    # 4️⃣ OPEN PRODUCT DETAILS
    # ==================================================
    first_product = driver.find_element(By.CSS_SELECTOR, ".product-item h2 a")
    product_name = first_product.text
    first_product.click()

    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-name")))
    print("✅ Product opened:", product_name)

    # ==================================================
    # 5️⃣ ADD TO CART
    # ==================================================
    # ==================================================
    # 5️⃣ ADD TO CART (HANDLE CONFIGURABLE PRODUCT)
    # ==================================================

    # Select Processor
    try:
        processor = wait.until(
            EC.element_to_be_clickable((By.ID, "product_attribute_1"))
        )
        processor.click()
        processor.find_elements(By.TAG_NAME, "option")[1].click()
        print("✅ Processor selected")
    except:
        pass

    # Select RAM
    try:
        ram = wait.until(
            EC.element_to_be_clickable((By.ID, "product_attribute_2"))
        )
        ram.click()
        ram.find_elements(By.TAG_NAME, "option")[1].click()
        print("✅ RAM selected")
    except:
        pass

    # Now Add To Cart
    add_btn = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='Add to cart']"))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", add_btn)

    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='Add to cart']"))
    ).click()

    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "content"))
    )

    print("✅ Added to cart")

    # ==================================================
    # 6️⃣ OPEN CART
    # ==================================================
    driver.find_element(By.CSS_SELECTOR, "span.cart-label").click()

    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "cart"))
    )
    print("✅ Cart opened")

    # ==================================================
    # 7️⃣ UPDATE CART
    # ==================================================
    qty = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input.qty-input"))
    )
    qty.clear()
    qty.send_keys("2")

    driver.find_element(By.NAME, "updatecart").click()
    print("✅ Cart updated")

    # ==================================================
    # 8️⃣ REMOVE ITEM
    # ==================================================
    remove = wait.until(
        EC.element_to_be_clickable((By.NAME, "removefromcart"))
    )
    remove.click()

    driver.find_element(By.NAME, "updatecart").click()
    print("✅ Item removed")

    # ==================================================
    # 9️⃣ LOGOUT
    # ==================================================
    wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Log out"))
    ).click()

    wait.until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Log in"))
    )

    print("✅ Logout successful")

