"""
Classe responsável por automatizar o preenchimento da tela de login.
"""
import time
import random

from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def fill_login_field(self, field_id, text):
        driver = self.driver
        field = driver.find_element(By.ID, field_id)
        for letter in text:
            field.send_keys(letter)
            time.sleep(round(random.uniform(0.1, 0.2), 3))
    
    def click_login_button(self, field_id):
        btn = self.driver.find_element(By.ID, field_id)
        time.sleep(2)
        btn.click()
    
    def login(self, username, password):
        self.fill_login_field("user-name", username)
        self.fill_login_field("password", password)
        self.click_login_button("login-button")