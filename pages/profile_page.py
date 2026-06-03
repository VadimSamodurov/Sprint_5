"""
Страница профиля пользователя
"""
from locators.ad_locators import AdLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.ad_locators = AdLocators

    def open(self):
        self.driver.get(f'{self.base_url}/profile')

    def is_my_ads_section_present(self):
        return self.is_element_present(self.ad_locators.MY_ADS_HEADER)

    def is_ad_present_in_profile(self):
        try:
            ads = self.find_elements(self.ad_locators.AD_ITEM)
            for ad in ads:
                if ad.is_displayed():
                    return True
            return False
        except Exception:
            return False

    def is_empty_ads_message_present(self):
        return self.is_element_present(self.ad_locators.EMPTY_ADS_MESSAGE)
