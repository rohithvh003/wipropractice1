from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from Day18_selenium.LoginPage import LoginPage

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 20)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

loginobj = LoginPage(driver)

loginobj.enter_username("Admin")
loginobj.enter_password("admin123")
loginobj.click_login()

wait.until(lambda d: "dashboard" in d.current_url)

print("Login Successful")
driver.quit()
