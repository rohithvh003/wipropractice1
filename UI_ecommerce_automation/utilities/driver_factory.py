import configparser
from selenium import webdriver


def get_driver():
    config = configparser.ConfigParser()
    config.read("config/config.ini")

    browser = config["DEFAULT"]["browser"]

    if browser == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    driver.maximize_window()
    return driver
