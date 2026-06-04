"""
Локаторы для создания объявления
"""


class AdLocators:
    MODAL_TITLE = ('xpath', '//*[contains(text(), "Чтобы разместить объявление, авторизуйтесь")]')

    AD_FORM_CONTAINER = ('css selector', '.createListingPage_createListingPageStyle__U-MJJ')
    AD_TITLE = ('css selector', 'input[placeholder="Название"][name="name"]')
    AD_DESCRIPTION = ('css selector', 'textarea[placeholder="Описание товара"][name="description"]')
    AD_PRICE = ('css selector', 'input[placeholder="Стоимость"][name="price"]')

    CATEGORY_DROPDOWN_ARROW = ('css selector', 'input[name="category"] ~ .dropDownMenu_arrowDown__pfGL1')
    CATEGORY_OPTION = ('xpath', '//button[@class="dropDownMenu_btn__o8ARs dropDownMenu_noDefault__wSKsP" and .//span[contains(text(), "{}")]]')

    CITY_DROPDOWN_ARROW = ('css selector', 'input[name="city"] ~ .dropDownMenu_arrowDown__pfGL1')
    CITY_OPTION = ('xpath', '//button[@class="dropDownMenu_btn__o8ARs dropDownMenu_noDefault__wSKsP" and .//span[contains(text(), "{}")]]')

    CONDITION_NEW = ('xpath', '//input[@name="condition" and @value="Новый"]')
    CONDITION_USED_LABEL = ('xpath', '//input[@name="condition" and @value="Б/У"]/following-sibling::label[@class="h2"]')
    CONDITION_NEW_LABEL = ('xpath', '//input[@name="condition" and @value="Новый"]/following-sibling::label[@class="h2"]')

    BTN_PUBLISH = ('xpath', '//button[@class="buttonPrimary inButtonText undefined inButtonText" and text()="Опубликовать"]')

    MY_ADS_SECTION = ('css selector', '.profilePage_listningBlock__Fi6E5')
    MY_ADS_HEADER = ('xpath', '//h1[@class="h1" and text()="Мои объявления"]')
    AD_ITEM = ('css selector', '.card')
    EMPTY_ADS_MESSAGE = ('xpath', '//h2[@class="h2" and text()="Здесь пока пусто..."]')
