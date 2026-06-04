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
        assert main_page.is_user_avatar_visible(), "Пользователь не авторизован"
        main_page.click_post_ad_button()

        ad_page = AdPage(driver)
        assert ad_page.is_ad_form_present(), "Форма создания объявления не отображается"

        ad_title = fake.word()
        ad_description = fake.sentence()
        ad_price = fake.random_int(min=100, max=10000)
        ad_category = "Хобби"
        ad_city = "Москва"

        ad_page.fill_ad_form(ad_title, ad_description, ad_price, ad_category, ad_city)
        ad_page.click_publish()

        import time
        time.sleep(2)
        main_page.open_profile()
        profile_page = ProfilePage(driver)
        assert profile_page.is_my_ads_section_visible(), "Секция 'Мои объявления' не отображается"
        assert profile_page.is_ad_created(ad_title), f"Объявление '{ad_title}' не найдено в профиле"
