from selenium import webdriver
from Day18_selenium.LoginPage_PageFactory import Loginpage_PageFactory
import time

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)

login_obj = Loginpage_PageFactory(driver)

login_obj.username("Admin")
login_obj.password("admin123")
login_obj.click_login()

time.sleep(5)
print("login successfully")
driver.quit()
