"""
Пакет страниц для автотестов
"""
from .base_page import BasePage
from .auth_page import AuthPage
from .main_page import MainPage
from .profile_page import ProfilePage
from .ad_page import AdPage

__all__ = ['BasePage', 'AuthPage', 'MainPage', 'ProfilePage', 'AdPage']
