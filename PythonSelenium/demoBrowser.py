from selenium import webdriver
from selenium.webdriver.common.by import By

#chrome driver  chrome cannot be invoked directly so it is having

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/")

print(driver.title)
print(driver.current_url)
driver.get("https://www.google.com")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()
