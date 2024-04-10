import time

from conftest import driver
from locators import StellarBurgerLocators
import settings
from data import StellarBurgerUserData
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructor:

    @staticmethod
    def login_from_login_page(driver):
        driver.get(settings.login_url)
        driver.find_element(*StellarBurgerLocators.EMAIL_FIELD).send_keys(StellarBurgerUserData.valid_user_email)
        driver.find_element(*StellarBurgerLocators.PASSWORD_FIELD).send_keys(StellarBurgerUserData.valid_user_password)
        driver.find_element(*StellarBurgerLocators.LOGIN_BUTTON_ON_LOGIN_PAGE).click()

    def test_constructor_opens_from_profile_with_constructor_button_successful(self, driver):
        TestConstructor.login_from_login_page(driver)
        driver.find_element(*StellarBurgerLocators.PROFILE_BUTTON_ON_MAIN_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(settings.logged_user_profile))
        assert driver.current_url == settings.logged_user_profile

    def test_constructor_opens_from_profile_with_click_on_logo_in_header_successful(self, driver):
        TestConstructor.login_from_login_page(driver)
        driver.find_element(*StellarBurgerLocators.PROFILE_BUTTON_ON_MAIN_PAGE).click()
        driver.find_element(*StellarBurgerLocators.LOGO_IN_HEADER).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(settings.main_url))
        assert expected_conditions.element_attribute_to_include(StellarBurgerLocators.LOGO_IN_HEADER, 'class')

    def test_constructor_switches_to_bun_section_successful(self, driver):
        driver.find_element(*StellarBurgerLocators.SAUCES_IN_SECTION_SELECTOR).click()
        driver.find_element(*StellarBurgerLocators.BUNS_IN_SECTION_SELECTOR).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(StellarBurgerLocators.BUNS_IN_SECTION_SELECTOR))
        parent = driver.find_element(*StellarBurgerLocators.PARENT_BUNS_IN_SECTION_SELECTOR)
        assert 'tab_type_current' in parent.get_attribute('class')

    def test_constructor_switches_to_filings_section_successful(self, driver):
        driver.find_element(*StellarBurgerLocators.FILLINGS_IN_SECTION_SELECTOR).click()
        time.sleep(3)
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(StellarBurgerLocators.FILLINGS_IN_SECTION_SELECTOR))
        parent = driver.find_element(*StellarBurgerLocators.PARENT_FILLINGS_IN_SECTION_SELECTOR)
        assert 'tab_type_current' in parent.get_attribute('class')

    def test_constructor_switches_to_sauces_section_successful(self, driver):
        driver.find_element(*StellarBurgerLocators.SAUCES_IN_SECTION_SELECTOR).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(StellarBurgerLocators.SAUCES_IN_SECTION_SELECTOR))
        parent = driver.find_element(*StellarBurgerLocators.PARENT_SAUCES_IN_SECTION_SELECTOR)
        assert 'tab_type_current' in parent.get_attribute('class')

