from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome
driver = webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()

# Verify title
assert "Your Store" in driver.title

# My Account → Register
driver.find_element(By.LINK_TEXT, "My Account").click()
driver.find_element(By.LINK_TEXT, "Register").click()

# Verify Register page heading
heading = driver.find_element(By.XPATH, "//h1").text
print("Heading:", heading)

assert heading == "Register Account"


# Click Continue without filling (to verify warning)
driver.find_element(By.XPATH, "//input[@value='Continue']").click()

warning = driver.find_element(By.CLASS_NAME, "alert-danger").text
print("Warning:", warning)
assert "Privacy Policy" in warning

# -----------------------------
# Your Personal Details
# -----------------------------

# First Name – 33 characters
driver.find_element(By.ID, "input-firstname").send_keys("A" * 33)
driver.find_element(By.XPATH, "//input[@value='Continue']").click()

fname_error = driver.find_element(By.CLASS_NAME, "text-danger").text
print("First Name Error:", fname_error)

driver.find_element(By.ID, "input-firstname").clear()
driver.find_element(By.ID, "input-firstname").send_keys("Akash")

# Last Name – 33 characters
driver.find_element(By.ID, "input-lastname").send_keys("B" * 33)
driver.find_element(By.XPATH, "//input[@value='Continue']").click()

lname_error = driver.find_element(By.CLASS_NAME, "text-danger").text
print("Last Name Error:", lname_error)

driver.find_element(By.ID, "input-lastname").clear()
driver.find_element(By.ID, "input-lastname").send_keys("V")

# Valid Email
driver.find_element(By.ID, "input-email").send_keys("akash123@test.com")

# Telephone (3–32 chars)
driver.find_element(By.ID, "input-telephone").send_keys("9876543210")

# -----------------------------
# Your Password
# -----------------------------
driver.find_element(By.ID, "input-password").send_keys("Test@123")
driver.find_element(By.ID, "input-confirm").send_keys("Test@123")

# -----------------------------
# Newsletter
# -----------------------------
driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='1']").click()

# Agree Privacy Policy
driver.find_element(By.NAME, "agree").click()

# Submit Registration
driver.find_element(By.XPATH, "//input[@value='Continue']").click()

# -----------------------------
# Verify Account Creation
# -----------------------------
success = driver.find_element(By.TAG_NAME, "h1").text
print("Success Message:", success)
assert success == "Your Account Has Been Created!"

time.sleep(2)
driver.quit()
