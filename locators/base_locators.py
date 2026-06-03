"""
Базовые локаторы для навигации по сайту
"""


class BaseLocators:
    HEADLINE_LOGIN = ('xpath', '//button[contains(text(), "Вход и регистрация")]')
    BTN_POST_AD = ('xpath', '//button[contains(text(), "Разместить объявление")]')
    USER_AVATAR = ('css selector', '.circleSmall')
    USER_NAME = ('xpath', '//div[contains(@class, "flexRow")]//span[contains(text(), "User")]/parent::*/parent::*')
    BTN_LOGOUT = ('xpath', '//button[@class="spanGlobal btnSmall" and text()="Выйти"]')
    BTN_PROFILE = ('xpath', '//div[contains(@class, "flexRow")]//button[@class="circleSmall"]')
