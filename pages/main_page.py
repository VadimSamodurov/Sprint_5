"""
Главная страница сайта
"""
from locators.base_locators import BaseLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_locators = BaseLocators

    def click_post_ad_button(self):
        self.click_element(self.base_locators.BTN_POST_AD)

    def click_login_button(self):
        self.click_element(self.base_locators.HEADLINE_LOGIN)

    def click_logout(self):
        self.click_element(self.base_locators.BTN_LOGOUT)

    def is_login_button_visible(self):
        return self.is_element_present(self.base_locators.HEADLINE_LOGIN)

    def is_user_avatar_visible(self):
        return self.is_element_present(self.base_locators.USER_AVATAR)

    def is_user_name_visible(self):
        return self.is_element_present(self.base_locators.USER_NAME)

    def is_logout_button_visible(self):
        return self.is_element_present(self.base_locators.BTN_LOGOUT)
