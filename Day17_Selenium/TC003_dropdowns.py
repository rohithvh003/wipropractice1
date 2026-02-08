from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.LINK_TEXT,"Desktops").click()
driver.find_element(By.LINK_TEXT,"Mac (1)").click()
dropdown=Select(driver.find_element(By.ID,"input-sort"))


for option in dropdown.options:
    print(option.text)
dropdown.select_by_index(4)