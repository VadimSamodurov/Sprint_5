"""
Тесты на функциональность выхода из системы
"""
import pytest
from faker import Faker
from pages.auth_page import AuthPage
from pages.main_page import MainPage

fake = Faker()


class TestLogout:

    def test_user_logout(self, driver):
        auth_page = AuthPage(driver)
        auth_page.open()
        auth_page.open_registration_form()

        test_email = fake.email()
        test_password = "TestPassword123"

        auth_page.fill_registration_form(test_email, test_password)

        main_page = MainPage(driver)
        main_page.click_logout()

        assert main_page.is_login_button_visible(), "Кнопка входа не отображается"
        assert not main_page.is_user_avatar_visible(), "Аватар пользователя все еще отображается"
