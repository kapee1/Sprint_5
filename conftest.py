import pytest
import settings
from selenium import webdriver
from locators import StellarBurgerLocators
from data import StellarBurgerUserData


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(settings.main_url)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope='function')
def login_from_login_page(driver):
    driver.get(settings.login_url)
    driver.find_element(*StellarBurgerLocators.EMAIL_FIELD).send_keys(StellarBurgerUserData.valid_user_email)
    driver.find_element(*StellarBurgerLocators.PASSWORD_FIELD).send_keys(StellarBurgerUserData.valid_user_password)
    driver.find_element(*StellarBurgerLocators.LOGIN_BUTTON_ON_LOGIN_PAGE).click()
