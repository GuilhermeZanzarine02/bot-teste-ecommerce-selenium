import time
import random

from selenium.webdriver.common.by import By

class Home_Page():
    def __init__(self, driver):
        self.driver = driver
    
    def select_product(self):
        driver = self.driver

        products = {
            0 : driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack"),
            1 : driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light"),
            2 : driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
            3 : driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket"),
            4 : driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie"),
            5 : driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
        }

        quantidade = random.randint(1, 3)

        sample = random.sample(list(products.keys()), quantidade)

        print(sample)

        for i in sample:
            products[i].click()
            time.sleep(2)
