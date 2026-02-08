from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()
print("title:",driver.title)
driver.get("https://google.com/")
time.sleep(5)
driver.back()
print("title is :",driver.title)
driver.forward()
print("title after forward:",driver.title)
