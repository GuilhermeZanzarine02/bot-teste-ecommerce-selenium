from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from utils.driver_factory import init_driver

def test_login_success():
    driver = init_driver()
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    assert "https://www.saucedemo.com/inventory.html" in driver.current_url

def test_login_failure_wrong_user():
    driver = init_driver()
    Login_page = LoginPage(driver)
    Login_page.login("guilherme", "secret_sauce")

    error_element = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]')
    error_text = error_element.text

    assert "Epic sadface: Username and password do not match any user in this service" in error_text

def test_login_failure_wrong_password():
    driver = init_driver()
    Login_page = LoginPage(driver)
    Login_page.login("standard_user", "secret_sauce123")

    error_element = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]')
    error_text = error_element.text

    assert "Epic sadface: Username and password do not match any user in this service" in error_text

def test_login_failure_no_username():
    driver = init_driver()
    Login_page = LoginPage(driver)
    Login_page.login("", "secret_sauce")

    error_element = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]')
    error_text = error_element.text

    assert "Epic sadface: Username is required" in error_text

def test_login_failure_no_password():
    driver = init_driver()
    Login_page = LoginPage(driver)
    Login_page.login("standard_user", "")

    error_element = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]')
    error_text = error_element.text

    assert "Epic sadface: Password is required" in error_text