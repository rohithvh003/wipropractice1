from selenium import webdriver
from Day18_selenium.Selenium_Lab11.lab3_PageFactory import Desktops_PageFactory
import time

def test_desktop_mac_flow():
    driver = webdriver.Firefox()
    driver.maximize_window()

    # Step 1: Open URL
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(3)
    # Create page object
    desktop_mac = Desktops_PageFactory(driver)

    # Step 2–5: Perform actions
    desktop_mac.open_mac_page()
    desktop_mac.sort_name_az()
    desktop_mac.add_first_product_to_cart()

    print("Desktop → Mac → Add to Cart flow completed")

    driver.quit()
