from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


driver=webdriver.Chrome()
driver.get("https://www.letcode.in/alert")
driver.find_element(By.ID,"accept").click()
time.sleep(3)
alert=driver.switch_to.alert
print(alert.text)
alert.accept()

driver.find_element(By.ID,"confirm").click()
time.sleep(3)
alert1=driver.switch_to.alert
print(alert1.text)
alert1.dismiss()

driver.find_element(By.ID,"prompt").click()
time.sleep(3)
alert2=driver.switch_to.alert
print("Alert message:", alert2.text)
name = "Rohith"
alert2.send_keys(name)
alert2.accept()
print("Text entered in alert:", name)
time.sleep(2)

driver.find_element(By.ID, "modern").click()

# Verify result text
alert_text = driver.find_element(By.CSS_SELECTOR, "p.title").text
print(alert_text)

assert alert_text == "Modern Alert - Some people address me as sweet alert as well"
print("Succesfully Verified",alert_text)


time.sleep(3)
driver.quit()