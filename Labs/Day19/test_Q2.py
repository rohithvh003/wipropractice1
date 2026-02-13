from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.options import Options as EdgeOptions

from Day20.driverfactory import GRIDURL

GRIDURL= "http://192.168.1.2:4444/wd/hub"

def get_driver(browser):
    if browser == "chrome":
        options = ChromeOptions
        options.add_argument("--disable-blink-features=AutomationControlled")

def get_driver(browser):
    if browser == "Edge":
        options = EdgeOptions
