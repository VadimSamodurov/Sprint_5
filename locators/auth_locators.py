"""
Локаторы для страницы авторизации и регистрации
"""


class AuthLocators:
    MODAL_TITLE_LOGIN = ('xpath', '//h1[contains(text(), "Войти")]')
    MODAL_TITLE_REG = ('xpath', '//h1[contains(text(), "Зарегистрироваться")]')

    BTN_NO_ACCOUNT = ('xpath', '//button[contains(text(), "Нет аккаунта")]')
    BTN_ALREADY_HAVE_ACCOUNT = ('xpath', '//button[contains(text(), "Уже есть аккаунт")]')

    LOGIN_EMAIL = ('css selector', 'input[name="email"][placeholder="Введите Email"]')
    LOGIN_PASSWORD = ('css selector', 'input[name="password"][placeholder="Пароль"]')
    BTN_LOGIN = ('xpath', '//button[@class="buttonPrimary inButtonText undefined inButtonText" and text()="Войти"]')

    REG_EMAIL = ('css selector', 'input[name="email"][placeholder="Введите Email"]')
    REG_PASSWORD = ('css selector', 'input[name="password"][placeholder="Пароль"]')
    REG_PASSWORD_CONFIRM = ('css selector', 'input[name="submitPassword"][placeholder="Повторите пароль"]')
    BTN_CREATE_ACCOUNT = ('xpath', '//button[contains(text(), "Создать аккаунт")]')

    ERROR_MESSAGE = ('xpath', '//*[contains(@class, "error") or contains(text(), "Ошиб") or contains(text(), "ошиб")]')
    ERROR_FIELD = ('css selector', '.input_inputError__fLUP9')
    VALIDATION_ERROR = ('xpath', '//*[contains(text(), "Ошиб")]')
