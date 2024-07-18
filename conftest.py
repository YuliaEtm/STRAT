import pytest
from selenium import webdriver
import os
from dotenv import load_dotenv


load_dotenv()
url = os.getenv('url')
login = os.getenv('login')
password = os.getenv('password')
name_theme = os.getenv('name_theme')
class_name = os.getenv('class_name')
name_chanel =os.getenv('name_chanel')

@pytest.fixture
def browser(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.addfinalizer(driver.close)
    return driver


