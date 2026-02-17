from UI_ecommerce_automation.pages.home_page import HomePage


def test_logout(setup):
    driver = setup
    home = HomePage(driver)

    home.logout()

    assert "Log in" in driver.page_source
