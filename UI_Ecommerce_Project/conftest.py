import pytest
import os
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from UI_Ecommerce_Project.Utilities.config_reader import ConfigReader
from UI_Ecommerce_Project.Utilities.logger import get_logger


# ==========================================
# DRIVER FIXTURE (Chrome + Edge + Firefox)
# ==========================================
@pytest.fixture
def driver(request):
    browser = ConfigReader.get_browser().lower()
    request.browser = browser

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--ignore-ssl-errors")
        options.add_argument("--allow-running-insecure-content")
        options.set_capability("acceptInsecureCerts", True)
        driver_instance = webdriver.Chrome(options=options)

    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--ignore-certificate-errors")
        options.set_capability("acceptInsecureCerts", True)
        driver_instance = webdriver.Edge(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        options.accept_insecure_certs = True
        driver_instance = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver_instance.maximize_window()
    driver_instance.implicitly_wait(ConfigReader.get_implicit_wait())
    driver_instance.get(ConfigReader.get_base_url())

    yield driver_instance
    driver_instance.quit()


# ==========================================
# USER FIXTURE
# ==========================================
@pytest.fixture
def user():
    return {
        "email": "test@test.com",
        "password": "Password123"
    }


# ==========================================
# BASE URL FIXTURE
# ==========================================
@pytest.fixture
def base_url():
    return ConfigReader.get_base_url()


# ==========================================
# LOGGER FIXTURE
# ==========================================
@pytest.fixture
def logger(request):
    logger_instance, log_file = get_logger(request.node.name)
    request.node.log_file = log_file
    return logger_instance


# ==========================================
# SCREENSHOT + LOG ATTACHMENT ON FAILURE
# ==========================================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":

        # ---------- Attach Logs ----------
        log_file = getattr(item, "log_file", None)   # ✅ FIXED HERE
        if log_file and os.path.exists(log_file):
            with open(log_file, "r") as f:
                log_content = f.read()
            if log_content:
                report.sections.append(("Execution Logs", log_content))

        # ---------- Screenshot on Failure ----------
        if report.failed:
            driver_instance = item.funcargs.get("driver")
            browser = getattr(item, "browser", "unknown_browser")

            if driver_instance:
                screenshots_dir = item.config.screenshots_dir

                timestamp = datetime.now().strftime("%H-%M-%S")
                screenshot_file = f"{item.name}_{browser}_{timestamp}.png"
                screenshot_path = os.path.join(screenshots_dir, screenshot_file)

                driver_instance.save_screenshot(screenshot_path)

                report.sections.append(
                    ("Failure Screenshot", f"Saved to: {screenshot_path}")
                )

                print(f"\n[✔] Screenshot captured: {screenshot_path}")


# ==========================================
# AUTO TIMESTAMPED REPORT GENERATION
# ==========================================
def pytest_configure(config):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    browser = ConfigReader.get_browser().lower()

    run_dir = os.path.join("reports", f"{browser}_{timestamp}")
    os.makedirs(run_dir, exist_ok=True)

    screenshots_dir = os.path.join(run_dir, "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)

    config.run_dir = run_dir
    config.screenshots_dir = screenshots_dir

    # Auto-generate HTML report path
    if not config.option.htmlpath:
        html_report_path = os.path.join(
            run_dir, f"report_{browser}_{timestamp}.html"
        )
        config.option.htmlpath = html_report_path
        print(f"[+] HTML report will be generated at: {html_report_path}")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )