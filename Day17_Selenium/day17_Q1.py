from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

# 1. Fill text boxes
driver.find_element(By.ID, "firstName").send_keys("Akash")
driver.find_element(By.ID, "lastName").send_keys("V")
driver.find_element(By.ID, "userEmail").send_keys("akash@test.com")
time.sleep(2)
# 2. Select radio button
driver.execute_script(
    "arguments[0].click();",
    driver.find_element(By.ID, "gender-radio-1")
)
time.sleep(2)
driver.find_element(By.ID, "userNumber").send_keys("8745963218")
#select check box
driver.execute_script("arguments[0].click();",
driver.find_element(By.ID, "hobbies-checkbox-1"))
time.sleep(1)
driver.find_element(By.ID,"currentAddress").send_keys("Banglore")
time.sleep(1)

driver.find_element(By.ID, "state").click()

# Type and select NCR
state = driver.find_element(By.ID, "react-select-3-input")
state.send_keys("NCR")



driver.execute_script("arguments[0].click();",
driver.find_element(By.ID, "submit"))

time.sleep(2)
# Verify submission
confirmation_text = driver.find_element(
    By.ID, "example-modal-sizes-title-lg"
).text

print("Confirmation message:", confirmation_text)
time.sleep(2)

driver.quit()
