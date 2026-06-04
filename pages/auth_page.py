"""
Страница авторизации и регистрации
"""
from selenium.webdriver.remote.webelement import WebElement
from locators.base_locators import BaseLocators
from locators.auth_locators import AuthLocators
from pages.base_page import BasePage


class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_locators = BaseLocators
        self.auth_locators = AuthLocators

    def open_login_modal(self):
        self.click_element(self.base_locators.HEADLINE_LOGIN)

    def open_registration_form(self):
        self.open_login_modal()
        self.click_element(self.auth_locators.BTN_NO_ACCOUNT)

    def fill_login_form(self, email, password):
        self.send_keys(self.auth_locators.LOGIN_EMAIL, email)
        self.send_keys(self.auth_locators.LOGIN_PASSWORD, password)
        self.click_element(self.auth_locators.BTN_LOGIN)

    def fill_registration_form(self, email, password):
        self.send_keys(self.auth_locators.REG_EMAIL, email)
        self.send_keys(self.auth_locators.REG_PASSWORD, password)
        self.send_keys(self.auth_locators.REG_PASSWORD_CONFIRM, password)
        self.click_element(self.auth_locators.BTN_CREATE_ACCOUNT)

    def is_error_message_shown(self):
        return self.is_element_present(self.auth_locators.ERROR_MESSAGE)

    def is_error_fields_highlighted(self):
        elements = self.find_elements(self.auth_locators.ERROR_FIELD)
        return len(elements) > 0

    def logout(self):
        self.click_element(self.base_locators.BTN_LOGOUT)
