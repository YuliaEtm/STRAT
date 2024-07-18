import time
from selenium.webdriver.common.by import By
from locators import locator_hint
from common.waits import wait_present, wait_not_present


def hint_first_page(browser, tab_name):
    """ Открывает первую страницу подсказки для любой вкладки
    переменная pic - 'текст' - название вкладки"""

    wait_present(browser, 'XPATH', "//div[contains(@class, 'Navigation')]/span[text()='" + tab_name + "']",
                 "отсутствует вкладка")
    browser.find_element(By.XPATH, "//div[contains(@class, 'Navigation')]/span[text()='" + tab_name + "']").click()
    time.sleep(5)
    wait_present(browser, 'XPATH', locator_hint.BADGE_HINT, "отсутствует иконка ? Подсказка")
    browser.find_element(By.XPATH, locator_hint.BADGE_HINT).click()


def hint_picture_day(browser):
    """ Проверка подсказок на вкладке Картина дня
    проверка на первой странице 2 блока текста, на второй - 3 блока текста"""
    wait_present(browser, 'XPATH', locator_hint.HINT_1, "не два текстовых блока на странице")
    wait_present(browser, 'XPATH', locator_hint.DOT_NAVIGATION_2, "отсутствует вторая точка страницы")
    browser.find_element(By.XPATH, locator_hint.DOT_NAVIGATION_2).click()
    wait_present(browser, 'XPATH', "//div[contains(@class, 'UserOnboarding_Item')][3]",
                 "не три текстовых блока на странице")


def hint_collection(browser):
    """ Проверка подсказок на вкладке Подборки
        проверка на первой странице 5 блоков текста, на второй - 0 блока текста"""

    wait_present(browser, 'XPATH', locator_hint.HINT_5, "отсутствует блок для подсказки")

    wait_present(browser, 'XPATH', locator_hint.DOT_NAVIGATION_2, "отсутствует вторая точка страницы")
    browser.find_element(By.XPATH, locator_hint.DOT_NAVIGATION_2).click()

    wait_not_present(browser, 'XPATH', locator_hint.PAGE_HINT, "отсутствуют тексты  подсказок")


# def hint_report(browser, tab_name):
#     """  Проверка подсказок на вкладке Отчет
#         проверка на первой странице 1 блок текста, на второй - 0 блока текста, на третьей - 0"""
#
#     hint_first_page(browser, tab_name)
#     wait_present(browser, 'XPATH', locator_hint.HINT_1,"отсутствует блок для подсказки")
#     wait_present(browser, 'XPATH', locator_hint.DOT_NAVIGATION_2, "отсутствует вторая точка страницы")
#     browser.find_element(By.XPATH, locator_hint.DOT_NAVIGATION_2).click()
#     wait_not_present(browser, 'XPATH', locator_hint.PAGE_HINT, "отсутствуют тексты  подсказок")
#     wait_present(browser, 'XPATH', locator_hint.DOT_NAVIGATION_3, "отсутствует третья точка страницы")
#     browser.find_element(By.XPATH, locator_hint.DOT_NAVIGATION_3).click()
#     time.sleep(5)
#     wait_not_present(browser, 'XPATH', locator_hint.PAGE_HINT]", "отсутствуют тексты  подсказок")
#
#
# def hint_settings(browser, tab_name):
#     """   Проверка подсказок на вкладке Настройки
#         проверка на первой странице 3 блока текста"""
#     hint_first_page(browser, tab_name)
#
#     wait_present(browser, 'XPATH', locator_hint.HINT_3,"отсутствуют тексты  подсказок")
