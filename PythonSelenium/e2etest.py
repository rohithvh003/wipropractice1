from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#chrome driver  chrome cannot be invoked directly so it is having

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")
time.sleep(2)

# //*[@id="menu"]/div[2]/ul/li[6]/a

driver.find_element(By.XPATH,"//*[@id='menu']/div[2]/ul/li[6]/a").click()

