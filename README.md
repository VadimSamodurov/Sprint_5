# Sprint_5 

## Стек технологий
- Python 3.x
- Selenium WebDriver 4.x
- pytest
- webdriver-manager
- Faker (для генерации тестовых данных)

## Установка зависимостей

```bash
pip install -r requirements.txt
```

## Структура проекта

```
Sprint_5/
├── locators/
│   ├── base_locators.py      # Базовые локаторы
│   ├── auth_locators.py      # Локаторы для авторизации и регистрации
│   └── ad_locators.py         # Локаторы для создания объявлений
├── pages/
│   ├── base_page.py          # Базовая страница
│   ├── auth_page.py          # Страница авторизации/регистрации
│   ├── main_page.py          # Главная страница
│   └── profile_page.py       # Страница профиля
├── tests/
│   ├── conftest.py           # Фикстуры для pytest
│   ├── test_registration.py # Тесты регистрации
│   ├── test_login.py         # Тесты входа
│   ├── test_logout.py        # Тесты выхода
│   └── test_create_ad.py     # Тесты создания объявления
├── requirements.txt
└── README.md
```

## Запуск тестов

Все тесты:
```bash
pytest tests/
```

Конкретный тестовый файл:
```bash
pytest tests/test_registration.py
```

С детальным выводом:
```bash
pytest tests/ -v
```

## Тестовые сценарии

### Регистрация пользователя
- Успешная регистрация
- Регистрация с email не по маске
- Регистрация существующего пользователя

### Авторизация
- Успешный вход в систему
- Выход из системы

