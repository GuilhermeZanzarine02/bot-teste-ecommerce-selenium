import time

from pages.home_page import Home_Page
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from utils.driver_factory import init_driver

def test_add_to_cart():
    driver = init_driver()
    home_page = Home_Page(driver)
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    time.sleep(3)
    home_page.select_product()

    button = driver.find_element(By.ID, "remove-sauce-labs-backpack")
    button_text = button.text

    assert "Remove" in button_text

