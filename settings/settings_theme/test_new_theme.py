import time
from common.autorization import authorization
import conftest
from common.waits import wait_present, wait_clickable, wait_not_present
from settings.settings_theme.new_theme import get_setting_theme, choose_language
from selenium.webdriver.common.by import By
from locators import locator_settings


def test_add_theme(browser):
    """  Заполнение формы добавления тематики
            name_theme - название
            class_name - класс событий (один из 'В мире','Политика','Экономика','Бизнес','Военная сфера','Культура и
            общество', 'Науки и технологии','Экология и ЧС', 'Прочие','Спорт и отдых'
            name_chanel - имя заранее созданного канала
            language_name- 'Русский', 'Английский', 'Немецкий', 'Китайский'"""
    # вкладка тематики открыта
    authorization(browser, conftest.login, conftest.password)
    get_setting_theme(browser)
    # кнопка добавить тематики
    wait_present(browser, 'XPATH', locator_settings.BUTTON_ADD_THEME, 'Кнопка добавить не найдена')
    browser.find_element(By.XPATH, locator_settings.BUTTON_ADD_THEME).click()
    wait_present(browser, 'XPATH', locator_settings.FORM_ADD_NEW_THEME, 'Форма  не открыта')
    # Поле название
    wait_present(browser, 'XPATH', locator_settings.NAME_THEME, 'Поле название не найдено')
    browser.find_element(By.XPATH, locator_settings.NAME_THEME).click()
    browser.find_element(By.XPATH, locator_settings.NAME_THEME).send_keys(conftest.name_theme)

    # Поле Класс событий
    wait_present(browser, 'XPATH', locator_settings.EVENT_CLASS, 'Поле название не найдено')
    browser.find_element(By.XPATH, locator_settings.EVENT_CLASS).click()
    wait_present(browser, 'XPATH', locator_settings.DROP_DOWN_CLASS, 'список выпал')
    browser.find_element(By.XPATH, locator_settings.CHOICE_CLASS).click()

    # Поле Каналы для публикаций
    wait_present(browser, 'XPATH', locator_settings.DROP_DOWN_CHANNEL_THEME, 'Поле канал не найдено')
    browser.find_element(By.XPATH, locator_settings.DROP_DOWN_CHANNEL_THEME).click()
    browser.find_element(By.XPATH, locator_settings.CHOICE_CHANNEL).click()
    # Закрыть выпадающий список
    browser.find_element(By.XPATH, locator_settings.EVENT_CLASS).click()
    wait_present(browser, 'XPATH', locator_settings.EVENT_CLASS, 'канал не выбран')

    # языки поле выбрать
    choose_language(browser, Русский=True, Английский=True, Немецкий=True, Китайский=False)
    # география публикаций не работает
    # Ключевые фразы и слова использовать ИИ
    browser.find_element(By.XPATH, locator_settings.SWITCH_BOX_AI).click()
    # Ключевые фразы и слова непонятная подсказка
    browser.find_element(By.XPATH, locator_settings.KEY_WORD).send_keys('день, вся ночь')
    # кнопка добавить в ключевых
    browser.find_element(By.XPATH, locator_settings.BUTTON_KEY_WORD).click()
    # проверка ключевых фраз //span[contains(text(),'день')]
    wait_present(browser, 'XPATH', "//span[contains(text(),'день')]", ' не выбран день')
    wait_present(browser, 'XPATH', "//span[contains(text(),'вся ночь')]", 'не выбрано вся ночь')

    # Источники публикаций
    browser.find_element(By.XPATH, locator_settings.SOURCE_OF_THE_PUBL).click()
    # Выбрать все каналы
    browser.find_element(By.XPATH, locator_settings.SELECT_ALL_CHANNEL).click()

    # кнопка добавить в источниках публикаций
    browser.find_element(By.XPATH, locator_settings.BUTTON_SOURCE).click()

    #  кнопка сохранить
    wait_clickable(browser, 'XPATH', locator_settings.BUTTON_NEW_THEME, 'не кликабелен')
    browser.find_element(By.XPATH, locator_settings.BUTTON_NEW_THEME).click()

    #  Тематика есть в списке
    wait_present(browser, 'XPATH', locator_settings.SEARCH_BY_NAME, ' тематика не создана')
    time.sleep(5)


def test_delete_theme(browser):
    """  Удаление тематики   """

    authorization(browser, conftest.login, conftest.password)
    get_setting_theme(browser)
    #  Тематика есть в списке
    wait_present(browser, 'XPATH', locator_settings.SEARCH_BY_NAME, ' тематика не создана')

    # time.sleep(5)
    browser.find_element(By.XPATH, locator_settings.BUTTON_DELETE_CHANNEL).click()
    # окно подтверждающее
    wait_present(browser, 'XPATH', locator_settings.CONFIRMATION_DELETED, ' окна  нет')
    browser.find_element(By.XPATH, locator_settings.BUTTON_CONFIRMATION_DELETED).click()
    # Ожидания
    wait_present(browser, 'XPATH', locator_settings.WAITING_DELETED, ' идет удаление')
    wait_present(browser, 'XPATH', locator_settings.WAITING_DELETED, ' удалено')
    wait_not_present(browser,'XPATH', locator_settings.SEARCH_BY_NAME, ' тематика не создана')

