import os
import pytest
import random
import string
import configparser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest_html import extras


# ---------------- READ CONFIG SAFELY ----------------

config = configparser.ConfigParser()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.join(BASE_DIR, "config", "config.ini")

if not os.path.exists(config_path):
    raise FileNotFoundError(f"Config file not found at: {config_path}")

config.read(config_path)

if "DEFAULT" not in config:
    raise KeyError("DEFAULT section missing in config.ini")

required_keys = ["base_url", "browser", "wait"]

for key in required_keys:
    if key not in config["DEFAULT"]:
        raise KeyError(f"Missing '{key}' in config.ini")

BASE_URL = config["DEFAULT"]["base_url"]
BROWSER = config["DEFAULT"]["browser"].lower()
WAIT_TIME = int(config["DEFAULT"]["wait"])


# ---------------- FIXTURE ----------------

@pytest.fixture
def setup():
    if BROWSER == "chrome":
        driver = webdriver.Chrome()
    elif BROWSER == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Browser must be chrome or firefox")

    driver.maximize_window()
    driver.get(BASE_URL)

    yield driver

    driver.quit()


# ---------------- REPORT ENHANCEMENT ----------------

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        extra = getattr(report, "extra", [])

        if report.passed:
            extra.append(extras.text("Test Passed Successfully ✅"))

        if report.failed:
            extra.append(extras.text("Test Failed ❌"))

            driver = item.funcargs.get("setup", None)
            if driver:
                screenshot_path = os.path.join(BASE_DIR, "tests", "failure.png")
                driver.save_screenshot(screenshot_path)
                extra.append(extras.image(screenshot_path))

        extra.append(extras.text(f"Base URL: {BASE_URL}"))
        extra.append(extras.text(f"Browser: {BROWSER}"))

        report.extra = extra


# ---------------- HELPER FUNCTION ----------------

def generate_email():
    random_string = ''.join(random.choices(string.ascii_lowercase, k=5))
    return f"auto_{random_string}@test.com"


# ---------------- COMPLETE END TO END TEST ----------------

def test_complete_ecommerce_flow(setup):
    """Verify full flow: Register → Login → Ad"""
