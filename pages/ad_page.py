"""
Страница создания объявления
"""
from locators.ad_locators import AdLocators
from pages.base_page import BasePage


class AdPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.ad_locators = AdLocators

    def is_auth_modal_shown(self):
        return self.is_element_present(self.ad_locators.MODAL_TITLE)

    def is_ad_form_present(self):
        return self.is_element_present(self.ad_locators.AD_FORM_CONTAINER)

    def fill_ad_form(self, title, description, price, category, city, is_new=True):
        self.send_keys(self.ad_locators.AD_TITLE, title)
        self.send_keys(self.ad_locators.AD_DESCRIPTION, description)
        self.send_keys(self.ad_locators.AD_PRICE, str(price))

        self.select_category(category)
        self.select_city(city)

        if is_new:
            self.click_element(self.ad_locators.CONDITION_NEW_LABEL)
        else:
            self.click_element(self.ad_locators.CONDITION_USED_LABEL)

    def select_category(self, category_text):
        self.click_element(self.ad_locators.CATEGORY_DROPDOWN_ARROW)
        option_locator = (self.ad_locators.CATEGORY_OPTION[0], self.ad_locators.CATEGORY_OPTION[1].format(category_text))
        self.click_element(option_locator)

    def select_city(self, city_text):
        self.click_element(self.ad_locators.CITY_DROPDOWN_ARROW)
        option_locator = (self.ad_locators.CITY_OPTION[0], self.ad_locators.CITY_OPTION[1].format(city_text))
        self.click_element(option_locator)

    def click_publish(self):
        self.click_element(self.ad_locators.BTN_PUBLISH)
