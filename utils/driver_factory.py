"""Função para iniciar o WebDriver"""

import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from utils.constants import get_url

def init_driver():
    """
    Inicializa o navegador e acessa a URL do site desejado, preparando o ambiente para automação ou testes. 
    """
    service = EdgeService(executable_path=r"C:\Users\gleme\Downloads\edgedriver_win64\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    url = get_url()
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
    return driver