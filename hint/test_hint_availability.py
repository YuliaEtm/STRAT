import conftest
from common.autorization import authorization
from hint_availability import hint_picture_day, hint_first_page, hint_collection
from selenium.webdriver.common.by import By
from locators import locator_hint
from common.waits import wait_present, wait_not_present


def test_hint_picture_day(browser):
    """ Проверка подсказок на вкладке Картина дня
        проверка на первой странице 2 блока текста, на второй - 3 блока текста"""
    authorization(browser, conftest.login, conftest.password)
    hint_first_page(browser, 'Картина дня')
    hint_picture_day(browser)


def test_hint_collection(browser):
    """ Проверка подсказок на вкладке Подборки
        проверка на первой странице 5 блоков текста, на второй - 0 блока текста"""
    authorization(browser, conftest.login, conftest.password)
    hint_first_page(browser, 'Подборки')
    hint_collection(browser)


def test_hint_report(browser):
    """  Проверка подсказок на вкладке Отчет
         проверка на первой странице 1 блок текста, на второй - 0 блока текста, на третьей - 0"""
    authorization(browser, conftest.login, conftest.password)
    hint_first_page(browser, 'Отчет')

    wait_present(browser, 'XPATH', locator_hint.HINT_1, "отсутствует блок для подсказки")
    wait_present(browser, 'XPATH', locator_hint.DOT_NAVIGATION_2, "отсутствует вторая точка страницы")
    browser.find_element(By.XPATH, locator_hint.DOT_NAVIGATION_2).click()
    wait_not_present(browser, 'XPATH', locator_hint.PAGE_HINT, "отсутствуют тексты  подсказок")
    wait_present(browser, 'XPATH', locator_hint.DOT_NAVIGATION_3, "отсутствует третья точка страницы")
    browser.find_element(By.XPATH, locator_hint.DOT_NAVIGATION_3).click()

    wait_not_present(browser, 'XPATH', locator_hint.PAGE_HINT, "отсутствуют тексты  подсказок")


def test_hint_settings(browser):
    """   Проверка подсказок на вкладке Настройки
          проверка на первой странице 3 блока текста"""
    authorization(browser, conftest.login, conftest.password)
    hint_first_page(browser, 'Настройки')
    wait_present(browser, 'XPATH', locator_hint.HINT_3, "отсутствуют тексты  подсказок")
