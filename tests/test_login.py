from conftest import driver
from locators import StellarBurgerLocators
from data import StellarBurgerUserData
import settings
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:

    @staticmethod
    def login_from_login_page(driver):
        driver.find_element(*StellarBurgerLocators.EMAIL_FIELD).send_keys(StellarBurgerUserData.valid_user_email)
        driver.find_element(*StellarBurgerLocators.PASSWORD_FIELD).send_keys(StellarBurgerUserData.valid_user_password)
        driver.find_element(*StellarBurgerLocators.LOGIN_BUTTON_ON_LOGIN_PAGE).click()

    def test_login_from_main_successful(self, driver):
        driver.find_element(*StellarBurgerLocators.LOGIN_BUTTON_ON_MAIN_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(settings.login_url))
        TestLogin.login_from_login_page(driver)
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(settings.main_url))

        assert driver.current_url == settings.main_url

    def test_login_from_profile_successful(self,driver):
        driver.find_element(*StellarBurgerLocators.LOGIN_BUTTON_ON_MAIN_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(settings.login_url))
        TestLogin.login_from_login_page(driver)
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(settings.main_url))

        assert driver.current_url == settings.main_url

    def test_login_from_registration_form_successful(self,driver):
        driver.get(settings.registration_url)
        driver.find_element(*StellarBurgerLocators.LOGIN_BUTTON_IN_HINT).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(settings.login_url))
        TestLogin.login_from_login_page(driver)
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(settings.main_url))

        assert driver.current_url == settings.main_url

    def test_login_from_password_recovery_form_successful(self,driver):
        driver.get(settings.password_recovery_url)
        driver.find_element(*StellarBurgerLocators.LOGIN_BUTTON_IN_HINT).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(settings.login_url))
        TestLogin.login_from_login_page(driver)
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(settings.main_url))

        assert driver.current_url == settings.main_url

