"""         Локаторы для вкладки Каналы
 """
import conftest

# Форма добавления нового канала
FORM_ADD_NEW_CHANNEL = "//form [@class='ChannelForm_ChannelForm__OzpFt']"
# Поле Идентификатор изменения
ADDRESS_CHANNEL_CHANGE = "//input[@name='address']"
# Поле название канала
NAME_CHANNEL = "//div [@class='ChannelForm_ChannelForm__inputs__ZctuR']/div/input[1]"
# Выпадающий список
DROP_DOWN_CHANNEL = "//div[@class='mantine-16xmw63 mantine-Select-itemsWrapper']"
# Поле название канала изменения
NAME_CHANNEL_CHANGE = "//input [@ name='name']"
# Поле тип
TYPE_CHANNEL = "//input[contains(@class, 'Select-input mantine-yxgw82')]"
# Кнопка сохранить изменения
BUTTON_SAVE_CHANGES = "//button[contains(text(),'Сохранить')]"
# Окно с предупреждением об удалении
WARNING_DELETE = "//div[@class='Modal_Content__SnPAY ConfirmDialog_ConfirmDialog__aFRG3']"
# Кнопка подтверждения удаления
BUTTON_DELETE = "//div[contains(@class,'ConfirmDialog')]//button[contains(text(),'Да')]"
# Кнопка добавить канал
BUTTON_NEW_CHANNEL = "//button[contains(text(),'Добавить канал')]"
# Кнопка добавить в форме нового канала
BUTTON_ADD_NEW_CHANNEL = "//div[@class='Modal_Content__SnPAY AddChannelModal_Modal__Cc2um']//button[@type='submit']"
# Вкладка каналы
TAB_CHANNELS = "//button[contains(text(),'Каналы')]"
"""     
Локаторы для вкладки Тематики       
"""

TAB_THEME = "//button[contains(text(),'Тематики')]"
# Кнопка добавления тематики
BUTTON_ADD_THEME = "//button[contains(text(),'Добавить тематику')]"
# Форма добавления канала
FORM_ADD_NEW_THEME = "//span[contains(text(),'Класс событий')]"
# Поле название
NAME_THEME = "//input[@placeholder = 'Выборы в США']"
# Поле Класс событий
EVENT_CLASS = "//input[@placeholder = 'Выбор класса']"
# Выпадающий список Класс событий
DROP_DOWN_CLASS = "//div[@class ='mantine-Select-dropdown mantine-rynikm']"
# Выбор класса Политика
dfff = "//div[contains(@class, 'itemsWrapper')]//div/span[text()='Политика']"
# выпадающий список Канал публикаций
DROP_DOWN_CHANNEL_THEME = "//div[@class='ChannelsInput_SelectInput__container__mnRdb']"
# языки поле выбрать
LANGUAGE_NAME = "//button[@class='LanguageInput_Anchor__6x95a']"
# Выпадающий список языки
DROP_DOWN_LANGUAGE = "//div[@class='Popover_Popover__b9PMk LanguageInput_Popover__BKVq2']"
# Чек бокс все языки
CHECK_BOX_ALL_LANGUAGE = "//label[contains(text(),'Все Языки')]"
# выбрать немецкий язык
CHECK_BOX_GERMAN = "//input[@id='language-de']"
# Поле языки
LANGUAGE = "//span[contains(text(),'Языки')]"
# Корзина немецкий язык
SELECTED_GERMAN = "//span[contains(text(),'Немецкий')]"
# Ключевые фразы и слова использовать ИИ
SWITCH_BOX_AI = "//button[contains(@class,'SwitchBox')]"
# Поле ключевые фразы и слова
KEY_WORD = "//input[contains(@class,'TextInputKeyWord')]"
# кнопка добавить в ключевых
BUTTON_KEY_WORD = "//div [@class='ThematicForm_AddKeyWord__2O1wN'][1]/button"
# Источники публикаций поле
SOURCE_OF_THE_PUBL = "//div[@class='PublicationSourceInput_Wrapper__5IRA0']"

SELECT_ALL_CHANNEL = "//div[@class ='PublicationSourceInput_Wrapper__5IRA0'] / div / div / div[2]"
# кнопка добавить в источниках публикаций
BUTTON_SOURCE = "//button[contains(@class,'PublicationSourceInput_AddButton')]"
# кнопка сохранить Тематику
BUTTON_NEW_THEME = "// div[ @class ='ThematicForm_Buttons__TN56S'] / button[1]"

# Выбор класса событий
CHOICE_CLASS = "//div[contains(@class, 'itemsWrapper')]//div/span[text()='" + conftest.class_name +"']"
# Выбор канала
CHOICE_CHANNEL = "//div[contains(@class, 'itemsWrapper')]/div[text()='" + conftest.name_chanel + "']"
# Поиск канала по имени в списке
SEARCH_BY_NAME="//span [@title='" + conftest.name_theme + "']"
# Кнопка удаление канала-корзина
BUTTON_DELETE_CHANNEL = "//span [@title='" + conftest.name_chanel + "']/../../../descendant::div[contains(@class ,'PositionBox')]"
# Окно предупреждение удаления
CONFIRMATION_DELETED = "// h2[contains(text(), 'Внимание')]"
# Подтверждение удаления кнопка ДА
BUTTON_CONFIRMATION_DELETED = "// button[contains(text(), 'Да')]"
# Ожидание удаления
WAITING_DELETED = "//div[contains(text(),'Удаляем тематику')]"
# сообщение - тематика удалена
THEME_DELETED = "//div[contains(text(),'Тематика удалена')]"
