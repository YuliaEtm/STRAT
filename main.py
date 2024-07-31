import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
from dotenv import load_dotenv
import locators.locator_authoriz
load_dotenv()
url = os.getenv('url')
login = os.getenv('login')
password = os.getenv('password')



driver = webdriver.Chrome()

driver.get(url)

driver.find_element(By.XPATH,locators.locator_authoriz.EMAIL_AUTHORIZ).send_keys(login)
driver.find_element(By.XPATH, locators.locator_authoriz.PASSWORD_AUTHORIZ).send_keys(password)
time.sleep(10)
driver.find_element(By.XPATH,locators.locator_authoriz.ENTER_BUTTON).click()
time.sleep(10)




