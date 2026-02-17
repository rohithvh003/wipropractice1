from UI_ecommerce_automation.pages.home_page import HomePage
from UI_ecommerce_automation.pages.login_page import LoginPage
from UI_ecommerce_automation.utilities.data_reader import get_data


def test_login(setup):
    driver = setup
    data = get_data()

    home = HomePage(driver)
    login = LoginPage(driver)

    home.open_login()
    login.login(data["login"]["email"], data["login"]["password"])

    assert "My account" in driver.page_source
