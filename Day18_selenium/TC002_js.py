from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://www.amazon.in")
# pop up msg
# js=driver.execute_script("alert('Hello Amazon')")
# print(js)

time.sleep(5)
driver.execute_script("window.scrollBy(0,900)")
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(10)
driver.quit()