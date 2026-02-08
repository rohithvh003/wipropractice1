from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")
print("title is:",driver.title)
time.sleep(3)


driver.find_element(By.LINK_TEXT,"Tablets").click()
print("title of another page:",driver.title)
time.sleep(3)

driver.back()
print("title is back to original page:",driver.title)
driver.get("https://google.com/")
time.sleep(3)
driver.forward()
print("title of forwarded to another site:",driver.title)

driver.back()
print("title of back to original site:",driver.title)


time.sleep(2)
driver.refresh()
print("title after refresh:",driver.title)
time.sleep(2)

driver.quit()
