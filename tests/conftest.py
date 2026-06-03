"""
Фикстуры для тестов
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
