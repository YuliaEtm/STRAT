from common.autorization import authorization
import conftest
from common.waits import wait_present
from settings.settings_channels.new_channel import get_setting_channel, delete_channel, change_name_channel, \
    change_address_channel, new_channel


def test_add_new_channel(browser):
    """Создание нового канала """

    authorization(browser, conftest.login, conftest.password)
    get_setting_channel(browser)
    new_channel(browser, 'proba', 'pr', 'Telegram')


def test_not_on_the_list(browser):
    name_channel = 'proba'
    """Канал виден в списке """
    authorization(browser, conftest.login, conftest.password)
    get_setting_channel(browser)
    wait_present(browser, 'XPATH', "//span[contains(text(),'" + name_channel + "' )]", 'канал не виден')


def test_delete_channel(browser):
    """Канал удален в списке """

    authorization(browser, conftest.login, conftest.password)
    get_setting_channel(browser)
    delete_channel(browser, 'proba2')


def test_change_name_channel(browser):
    """Название канала изменено в списке """

    authorization(browser, conftest.login, conftest.password)
    get_setting_channel(browser)
    change_name_channel(browser, 'proba', 'proba2')


def test_change_address_channel(browser):
    """Идентификатор изменен """
    authorization(browser, conftest.login, conftest.password)
    get_setting_channel(browser)
    change_address_channel(browser, 'proba2', 'pr2', 'pr')
