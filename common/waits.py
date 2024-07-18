from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

wait_tame = 20

#WebDriverWait(driver, timeout=10).until(expected_conditions.presence_of_element_located(By.ID,'Element'))
#ожидание наличия элемента
def wait_present(browser,selector_cat,selector,message):
    if selector_cat =='XPATH':
        return WebDriverWait(browser, wait_tame).until(expected_conditions.presence_of_element_located((
            By.XPATH,selector)),message)
    if selector_cat == 'ID':
        return WebDriverWait(browser, wait_tame).until(expected_conditions.presence_of_element_located((
            By.ID, selector)), message)


#кликабелен
def wait_clickable(browser,selector_cat,selector,message):
    if selector_cat =='XPATH':
        return WebDriverWait(browser, wait_tame).until(expected_conditions.element_to_be_clickable((
            By.XPATH,selector)),message)
    if selector_cat == 'ID':
        return WebDriverWait(browser, wait_tame).until(expected_conditions.element_to_be_clickable((
            By.ID, selector)), message)

#элемент не виден
def wait_not_present(browser,selector_cat,selector,message):
    if selector_cat =='XPATH':
        return WebDriverWait(browser, wait_tame).until(expected_conditions.invisibility_of_element_located((
            By.XPATH,selector)),message)
    if selector_cat == 'ID':
        return WebDriverWait(browser, wait_tame).until(expected_conditions.invisibility_of_element_located((
            By.ID, selector)), message)


#наличие текста в элементе text = 'любой набор букв'
def wait_text(browser,selector_cat,selector,text,message):
    if selector_cat =='XPATH':
        return WebDriverWait(browser, wait_tame).until(expected_conditions.text_to_be_present_in_element_value((
            By.XPATH,selector), text), message)
    if selector_cat == 'ID':
        return WebDriverWait(browser, wait_tame).until(expected_conditions.text_to_be_present_in_element_value((
            By.ID, selector), text), message)


