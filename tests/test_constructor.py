from locators import StellarBurgerLocators
import settings
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver, login_from_login_page


class TestConstructor:

    def test_constructor_opens_from_profile_with_constructor_button_successful(self, driver, login_from_login_page):
        driver.find_element(*StellarBurgerLocators.PROFILE_BUTTON_ON_MAIN_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(settings.logged_user_profile))
        assert driver.current_url == settings.logged_user_profile

    def test_constructor_opens_from_profile_with_click_on_logo_in_header_successful(self, driver, login_from_login_page):
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
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(StellarBurgerLocators.FILLINGS_IN_SECTION_SELECTOR))
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

