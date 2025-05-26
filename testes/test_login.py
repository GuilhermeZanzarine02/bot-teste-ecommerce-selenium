import pytest

from pages.login_page import LoginPage
from utils.driver_factory import init_driver

def test_login_success():
    driver = init_driver()
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    assert "https://www.saucedemo.com/inventory.html" in driver.current_url