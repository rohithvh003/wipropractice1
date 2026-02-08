from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://letcode.in/frame")
driver.implicitly_wait(10)

# Switch to iframe and enter text
iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)
driver.find_element(By.NAME, "fname").send_keys("Rohith")
driver.find_element(By.NAME, "lname").send_keys("v h")


driver.switch_to.default_content()
insight = driver.find_element(By.XPATH, "//p[text()=' Insight ']").is_displayed()
print("Back to main page")

# Open new tab
parent = driver.current_window_handle
driver.switch_to.new_window("tab")
driver.get("https://www.google.com")

# Switch windows and print titles
for win in driver.window_handles:
    driver.switch_to.window(win)
    print("Window title:", driver.title)

# Close child window and return to parent
driver.close()
driver.switch_to.window(parent)
print("Returned to parent window:", driver.title)

time.sleep(2)
driver.quit()
