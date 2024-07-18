from common.waits import wait_present, wait_not_present
from selenium.webdriver.common.by import By
from locators import locator_hint
from locators import locator_settings


def get_setting_channel(browser):
    """ Переход на вкладку Настройки-каналы"""
    wait_present(browser, 'XPATH', locator_hint.SETTINGS, 'Вкладка настройки не найдена')
    browser.find_element(By.XPATH, locator_hint.SETTINGS).click()
    wait_present(browser, 'XPATH', locator_settings.TAB_CHANNELS, 'Вкладка каналы не найдена')
    browser.find_element(By.XPATH, locator_settings.TAB_CHANNELS).click()
    wait_present(browser, 'XPATH', "//input[@placeholder='Поиск по каналам']", 'Вкладка каналы не открыта')


def new_channel(browser, name_channel, address, type_channel):
    """Новый канал, name_channel- имя  канала
    address- ссылка, type_channel - тип источника"""
    wait_present(browser, 'XPATH', locator_settings.BUTTON_NEW_CHANNEL, 'кнопка добавить канал не найдена')
    browser.find_element(By.XPATH, locator_settings.BUTTON_NEW_CHANNEL).click()
    wait_present(browser, 'XPATH', locator_settings.FORM_ADD_NEW_CHANNEL, 'Форма добавления канала не найдена')
    browser.find_element(By.XPATH, locator_settings.NAME_CHANNEL).send_keys(name_channel)
    # выпадающий список
    browser.find_element(By.XPATH, locator_settings.TYPE_CHANNEL).click()
    wait_present(browser, 'XPATH', locator_settings.DROP_DOWN_CHANNEL, 'список не виден')
    browser.find_element(By.XPATH, "//div[contains(@class, 'itemsWrapper')]/div[text()='" + type_channel + "']").click()
    wait_not_present(browser, 'XPATH', locator_settings.DROP_DOWN_CHANNEL, 'список не закрыт')
    # ввод поля Идентификатор
    browser.find_element(By.XPATH, locator_settings.ADDRESS_CHANNEL_CHANGE).send_keys(address)
    # Кнопка добавить
    browser.find_element(By.XPATH, locator_settings.BUTTON_ADD_NEW_CHANNEL).click()
    wait_not_present(browser, 'XPATH', locator_settings.FORM_ADD_NEW_CHANNEL, 'Форма добавления канала не закрыта')
    # Канал виден в списке
    wait_present(browser, 'XPATH', "//span[contains(text(),'" + name_channel + "' )]", 'канал не виден')


def delete_channel(browser, name_channel):
    """ Удаление канала
    name_channel - имя канала"""
    wait_present(browser, 'XPATH', "//span[contains(text(),'" + name_channel + "' )]", 'канал не виден')
    browser.find_element(By.XPATH,
                         "//span[contains(text(),'" + name_channel + "' )]/../../../../div[4]/div/div[2]").click()
    wait_present(browser, 'XPATH', locator_settings.WARNING_DELETE, 'Предупреждение не видно')
    wait_present(browser, 'XPATH', locator_settings.BUTTON_DELETE, 'Кнопка удалить не видна')
    browser.find_element(By.XPATH, locator_settings.BUTTON_DELETE).click()
    wait_not_present(browser, 'XPATH', locator_settings.WARNING_DELETE, 'Предупреждение не закрыто')
    # Проверка
    wait_not_present(browser, 'XPATH', "//span[contains(text(),'" + name_channel + "' )]", 'канал не удален')


def change_name_channel(browser, name_channel, new_name_channel):
    """ Редактирование имени канала
    name_channel- старое имя, new_name_channel - новое имя"""
    wait_present(browser, 'XPATH', "//span[contains(text(),'" + name_channel + "' )]", 'канал не виден')
    browser.find_element(By.XPATH, "//span[contains(text(),'" + name_channel + "' )]").click()
    # убедится что поле заполнено старыми данными
    text_name_channel = browser.find_element(By.XPATH, locator_settings.NAME_CHANNEL_CHANGE).get_attribute("value")
    assert text_name_channel == name_channel

    browser.find_element(By.XPATH, locator_settings.NAME_CHANNEL_CHANGE).clear()
    browser.find_element(By.XPATH, locator_settings.NAME_CHANNEL_CHANGE).send_keys(new_name_channel)
    wait_present(browser, 'XPATH', locator_settings.BUTTON_SAVE_CHANGES, 'кнопка не видна')
    browser.find_element(By.XPATH, locator_settings.BUTTON_SAVE_CHANGES).click()
    wait_present(browser, 'XPATH', "//span[contains(text(),'" + new_name_channel + "' )]", 'канал не виден')


def change_address_channel(browser, name_channel, new_address_channel, address_channel):
    """ Редактирование ссылки канала
        name_channel- старое имя, new_address_channel -новый адрес,
        address_channel - адрес """
    wait_present(browser, 'XPATH', "//span[contains(text(),'" + name_channel + "' )]", 'канал виден')
    browser.find_element(By.XPATH, "//span[contains(text(),'" + name_channel + "' )]").click()
    address_name_channel = browser.find_element(By.XPATH, locator_settings.ADDRESS_CHANNEL_CHANGE).get_attribute(
        "value")
    assert address_name_channel == address_channel
    browser.find_element(By.XPATH, locator_settings.ADDRESS_CHANNEL_CHANGE).clear()
    browser.find_element(By.XPATH, locator_settings.ADDRESS_CHANNEL_CHANGE).send_keys(new_address_channel)
    browser.find_element(By.XPATH, locator_settings.BUTTON_SAVE_CHANGES).click()
