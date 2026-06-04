"""
Базовая страница с общими методами
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    BASE_URL = 'https://qa-desk.education-services.ru/'

    def __init__(self, driver):
        self.driver = driver
        self.base_url = self.BASE_URL

    def open(self):
        self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click_element(self, locator, time=10):
        element = self.find_element(locator, time)
        self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, text, time=10):
        element = self.find_element(locator, time)
        element.clear()
        element.send_keys(text)

    def is_element_present(self, locator, time=10):
        try:
            self.find_element(locator, time)
            return True
        except Exception:
            return False

    def wait_for_element_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator)
        )
