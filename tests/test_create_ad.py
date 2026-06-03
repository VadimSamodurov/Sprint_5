"""
Тесты на функциональность создания объявления
"""
import pytest
from pages.main_page import MainPage
from pages.auth_page import AuthPage
from pages.ad_page import AdPage
from pages.profile_page import ProfilePage
from pages.base_page import BasePage
from faker import Faker

fake = Faker()


class TestCreateAd:

    def test_create_ad_unauthorized(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_post_ad_button()

        ad_page = AdPage(driver)
        assert ad_page.is_auth_modal_shown(), "Модальное окно авторизации не отображается"

    def test_create_ad_authorized(self, driver):
        auth_page = AuthPage(driver)
        auth_page.open()
        auth_page.open_registration_form()

        test_email = fake.email()
        test_password = "TestPassword123"

        auth_page.fill_registration_form(test_email, test_password)

        main_page = MainPage(driver)

        main_page.click_post_ad_button()
