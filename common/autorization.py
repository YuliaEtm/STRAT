import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from  locators import locator_authoriz
from  common.waits import wait_clickable, wait_present
import conftest


def authorization(browser,login,password):
    browser.get(conftest.url)
    wait_present(browser,'XPATH', locator_authoriz.EMAIL_AUTHORIZ, 'отсутствует поле логин')
    browser.find_element(By.XPATH,locator_authoriz.EMAIL_AUTHORIZ).send_keys(login)
    browser.find_element(By.XPATH, locator_authoriz.PASSWORD_AUTHORIZ).send_keys(password)

    wait_clickable(browser,'XPATH',locator_authoriz.ENTER_BUTTON,'  не нажимается')
    browser.find_element(By.XPATH,locator_authoriz.ENTER_BUTTON).click()
    wait_present(browser,'XPATH',locator_authoriz.LOGIN_VERIFICATION,' нет перехода на стр зарегистрированного пользователя')




