from conftest import driver
from locators import StellarBurgerLocators
from data import StellarBurgerUserData
import settings
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestProfile:

    @staticmethod
    def login_from_login_page(driver):
        driver.get(settings.login_url)
        driver.find_element(*StellarBurgerLocators.EMAIL_FIELD).send_keys(StellarBurgerUserData.valid_user_email)
        driver.find_element(*StellarBurgerLocators.PASSWORD_FIELD).send_keys(StellarBurgerUserData.valid_user_password)
        driver.find_element(*StellarBurgerLocators.LOGIN_BUTTON_ON_LOGIN_PAGE).click()

    def test_navigation_to_profile_with_logged_user_successful(self, driver):
        TestProfile.login_from_login_page(driver)
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(settings.main_url))
        driver.find_element(*StellarBurgerLocators.PROFILE_BUTTON_ON_MAIN_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(settings.logged_user_profile))
        assert driver.current_url == settings.logged_user_profile

    def test_navigation_to_profile_without_login_failed(self, driver):
        driver.find_element(*StellarBurgerLocators.PROFILE_BUTTON_ON_MAIN_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(settings.login_url))
        assert driver.current_url == settings.login_url

    def test_logout_from_account_successful(self, driver):
        TestProfile.login_from_login_page(driver)
        driver.find_element(*StellarBurgerLocators.PROFILE_BUTTON_ON_MAIN_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(settings.logged_user_profile))
        driver.find_element(*StellarBurgerLocators.LOG_OUT_BUTTON_IN_PROFILE).click()
        WebDriverWait(driver,3).until(expected_conditions.url_to_be(settings.login_url))
        assert expected_conditions.presence_of_element_located(StellarBurgerLocators.LOGIN_BUTTON_ON_LOGIN_PAGE)

