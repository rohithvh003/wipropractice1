from selenium import webdriver
from TC001 import Desktops
import time

def test_desktop_mac_flow():
    driver = webdriver.Firefox()
    driver.maximize_window()

    # Step 1: Open URL
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(3)

    desktop_mac = Desktops(driver)
    time.sleep(3)
    # Step 2: Desktops → Mac
    desktop_mac.open_mac_page()

    # # Step 3: Verify Mac heading (ADDED)
    # assert desktop_mac.verify_mac_heading()
    # print("Mac heading verified")

    # Step 4: Sort Name (A-Z)
    desktop_mac.sort_name_az()
    time.sleep(3)
    # Step 5: Add to Cart
    desktop_mac.add_first_product_to_cart()
    time.sleep(3)
    # Step 6: Search product (CHANGED Mobile → Monitors)
    desktop_mac.search_product("Monitors")

    # Step 7: Advanced search
    desktop_mac.advanced_search()

    print("Full flow executed successfully")

    driver.quit()
