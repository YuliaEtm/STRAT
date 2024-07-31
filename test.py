from  common.autorization import authorization
import  conftest


def test_authorzation_pozitive(browser):
    authorization(browser,conftest.login,conftest.password)

