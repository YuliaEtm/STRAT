import time

from common.waits import wait_present, wait_not_present
from selenium.webdriver.common.by import By
from locators import locator_hint
from locators import locator_settings


def get_setting_theme(browser):
    # Переход на вкладку тематики
    wait_present(browser, 'XPATH', locator_hint.SETTINGS, 'Вкладка настройки не найдена')
    browser.find_element(By.XPATH, locator_hint.SETTINGS).click()
    wait_present(browser, 'XPATH', locator_settings.TAB_THEME, 'Вкладка каналы не найдена')
    browser.find_element(By.XPATH, locator_settings.TAB_THEME).click()
    wait_present(browser, 'XPATH', "//input[@placeholder='Поиск по тематикам']", 'Вкладка тематики не открыта')


def language(browser, **dict_language):
    for key, value in dict_language.items():
        if key == 'Русский' and value == True:
            browser.find_element(By.XPATH, "//label[contains(text(),'Русский')]").click()
        elif key == 'Английский' and value is True:
            browser.find_element(By.XPATH, "//label[contains(text(),'Английский')]").click()
        elif key == 'Немецкий' and value is True:
            browser.find_element(By.XPATH, "//label[contains(text(),'Немецкий')]").click()
        elif key == 'Китайский' and value is True:
            browser.find_element(By.XPATH, "//label[contains(text(),'Китайский')]").click()
# проверки наличия и ожидания
def checking_language(browser, **dict_language):
    for key, value in dict_language.items():
        if key == 'Русский' and value == True:
            wait_present(browser, 'XPATH', "//span[contains(text(),'Русский')]", 'выбран Русский')
        elif key == 'Английский' and value is True:
            wait_present(browser, 'XPATH', "//span[contains(text(),'Английский')]", 'выбран Английский')
        elif key == 'Немецкий' and value is True:
            wait_present(browser, 'XPATH', "//span[contains(text(),'Немецкий')]", 'выбран немецкий')
        elif key == 'Китайский' and value is True:
            wait_present(browser, 'XPATH', "//span[contains(text(),'Китайский')]", 'выбран Китайский')

def choose_language(browser,**dict_language):

    # языки поле выбрать
    wait_present(browser, 'XPATH', locator_settings.LANGUAGE_NAME, 'Поле языки не найдено')
    browser.find_element(By.XPATH, locator_settings.LANGUAGE_NAME).click()
    # наличие выпадающего списка
    wait_present(browser, 'XPATH', locator_settings.DROP_DOWN_LANGUAGE, 'список языки не выпал')
    # Чек бокс все языки снять//label[contains(text(),'Все Языки')]
    browser.find_element(By.XPATH, locator_settings.CHECK_BOX_ALL_LANGUAGE).click()
    language (browser, **dict_language)
    # не закрывается нужен клик на свободное поле Языки
    browser.find_element(By.XPATH, locator_settings.LANGUAGE).click()
    # проверка, что выпадающий убрался
    wait_not_present(browser, 'XPATH', locator_settings.DROP_DOWN_LANGUAGE, 'список языки остался')
    # Проверка, что язык выбран
    checking_language(browser,**dict_language)


def choose_class(browser, class_name):
    # Поле Класс событий
    wait_present(browser, 'XPATH', locator_settings.EVENT_CLASS, 'Поле название не найдено')
    browser.find_element(By.XPATH, locator_settings.EVENT_CLASS).click()
    wait_present(browser, 'XPATH', locator_settings.DROP_DOWN_CLASS, 'список выпал')
    browser.find_element(By.XPATH,
                         "//div[contains(@class, 'itemsWrapper')]//div/span[text()='" + class_name + "']").click()
