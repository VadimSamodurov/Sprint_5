"""
Тесты на функциональность регистрации пользователя
"""
import pytest
from faker import Faker
from pages.main_page import MainPage
from pages.auth_page import AuthPage

fake = Faker()


class TestRegistration:

    def test_successful_registration(self, driver):
        auth_page = AuthPage(driver)
        auth_page.open()
        auth_page.open_registration_form()

        test_email = fake.email()
        test_password = "TestPassword123"

        auth_page.fill_registration_form(test_email, test_password)

        main_page = MainPage(driver)
        assert main_page.is_user_avatar_visible(), "Аватар пользователя не отображается"
        assert main_page.is_logout_button_visible(), "Кнопка Выйти не отображается"

    def test_registration_with_invalid_email_format(self, driver):
        auth_page = AuthPage(driver)
        auth_page.open()
        auth_page.open_registration_form()

        auth_page.fill_registration_form("invalid_email", "TestPassword123")

        assert auth_page.is_error_fields_highlighted(), "Поля не выделены красным"
        assert auth_page.is_error_message_shown(), "Сообщение об ошибке не отображается"

    def test_registration_existing_user(self, driver):
        auth_page = AuthPage(driver)
        auth_page.open()
        auth_page.open_registration_form()

        test_email = "test@exists.com"
        test_password = "TestPassword123"

        auth_page.send_keys(auth_page.auth_locators.REG_EMAIL, test_email)
        auth_page.send_keys(auth_page.auth_locators.REG_PASSWORD, test_password)
        auth_page.send_keys(auth_page.auth_locators.REG_PASSWORD_CONFIRM, test_password)

        auth_page.click_element(auth_page.auth_locators.BTN_CREATE_ACCOUNT)

        assert auth_page.is_error_fields_highlighted(), "Поля не выделены красным"
        assert auth_page.is_error_message_shown(), "Под полем Email не отображается сообщение Ошибка"
