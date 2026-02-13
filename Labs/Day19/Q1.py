from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://tutorialsninja.com/demo/")
print("Website opened")

wait = WebDriverWait(driver, 10)
my_account = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account")))
print("My Account is clickable")
my_account.click()

fluent_wait = WebDriverWait(driver, 10, poll_frequency=2)
login = fluent_wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
print("Login is clickable")
login.click()

print("Execution completed")
driver.quit()
