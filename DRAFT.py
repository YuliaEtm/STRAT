import time
from common.autorization import authorization
import conftest
from common.waits import wait_present, wait_not_present
from settings.settings_theme.new_theme import get_setting_theme
from selenium.webdriver.common.by import By
from locators import locator_settings
from selenium.webdriver.common.action_chains import ActionChains


def test_add_theme1(browser):
    # вкладка тематики открыта
    authorization(browser, conftest.login, conftest.password)
    get_setting_theme(browser)
    # кнопка добавить тематики
    wait_present(browser, 'XPATH', locator_settings.BUTTON_ADD_THEME, 'Кнопка добавить не найдена')
    browser.find_element(By.XPATH, locator_settings.BUTTON_ADD_THEME).click()
    wait_present(browser, 'XPATH', locator_settings.FORM_ADD_NEW_THEME, 'Форма  не открыта')

    # Поле Класс событий
    wait_present(browser, 'XPATH', locator_settings.EVENT_CLASS, 'Поле название не найдено')
    browser.find_element(By.XPATH, locator_settings.EVENT_CLASS).click()
    wait_present(browser, 'XPATH', locator_settings.DROP_DOWN_CLASS, 'список выпал')
    action = ActionChains(browser)
    action.move_to_element(
        browser.find_element(By.XPATH, "//div[contains(@class, 'itemsWrapper')]//div/span[text()='Прочее']")).perform()
    time.sleep(5)


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

#dict_language = {'Русский': False, 'Английский': True, 'Немецкий': True, 'Китайский': False}


def test_add_theme2(browser):
    # вкладка тематики открыта
    authorization(browser, conftest.login, conftest.password)
    get_setting_theme(browser)
    # кнопка добавить тематики
    wait_present(browser, 'XPATH', locator_settings.BUTTON_ADD_THEME, 'Кнопка добавить не найдена')
    browser.find_element(By.XPATH, locator_settings.BUTTON_ADD_THEME).click()
    wait_present(browser, 'XPATH', locator_settings.FORM_ADD_NEW_THEME, 'Форма  не открыта')

    # языки поле выбрать //button[@class='LanguageInput_Anchor__6x95a']
    wait_present(browser, 'XPATH', locator_settings.LANGUAGE_NAME, 'Поле языки не найдено')
    browser.find_element(By.XPATH, locator_settings.LANGUAGE_NAME).click()
    # наличие выпадающего списка
    wait_present(browser, 'XPATH', locator_settings.DROP_DOWN_LANGUAGE,
                 'список языки не выпал')
    # Чек бокс все языки снять//label[contains(text(),'Все Языки')]
    browser.find_element(By.XPATH, locator_settings.CHECK_BOX_ALL_LANGUAGE).click()
    language (browser, Русский=False, Английский=True, Немецкий=True, Китайский=False)
    time.sleep(5)
    # список выбора сам не закрывается нужен клик на свободное поле Языки
    browser.find_element(By.XPATH, locator_settings.LANGUAGE).click()
    # проверка, что выпадающий убрался
    time.sleep(5)
    wait_not_present(browser, 'XPATH', locator_settings.DROP_DOWN_LANGUAGE, 'список языки остался')
    # # Проверка, что немецкий выбран
    wait_present(browser, 'XPATH', "//span[contains(text(),'Немецкий')]", 'выбран немецкий')
