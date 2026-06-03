"""
Тесты на функциональность входа в систему
"""
import pytest
from faker import Faker
from pages.main_page import MainPage
from pages.auth_page import AuthPage

fake = Faker()


class TestLogin:

    def test_successful_login(self, driver):
        test_email = fake.email()
        test_password = "TestPassword123"

        auth_page = AuthPage(driver)
        auth_page.open()
        auth_page.open_registration_form()
        auth_page.fill_registration_form(test_email, test_password)

        main_page = MainPage(driver)
        main_page.click_logout()

        main_page.click_login_button()

        auth_page.fill_login_form(test_email, test_password)

        assert main_page.is_user_avatar_visible(), "Аватар пользователя не отображается"
        assert main_page.is_logout_button_visible(), "Кнопка Выйти не отображается"
