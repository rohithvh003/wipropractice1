import pytest
import configparser
import os
from datetime import datetime
from UI_ecommerce_automation.utilities.driver_factory import get_driver


@pytest.fixture
def setup():
    driver = get_driver()

    config = configparser.ConfigParser()
    config.read("config/config.ini")
    driver.get(config["DEFAULT"]["base_url"])

    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs["setup"]
        os.makedirs("screenshots", exist_ok=True)
        driver.save_screenshot(f"screenshots/fail_{datetime.now().timestamp()}.png")
