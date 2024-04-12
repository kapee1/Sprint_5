import pytest
from conftest import driver
from locators import StellarBurgerLocators
import settings
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helper import correct_user_data_generator


class TestRegistration:

    def test_registration_success(self, driver):
        driver.get(settings.registration_url)
        user = correct_user_data_generator()
        driver.find_element(*StellarBurgerLocators.NAME_FIELD).send_keys(user['name'])
        driver.find_element(*StellarBurgerLocators.EMAIL_FIELD).send_keys(user['email'])
        driver.find_element(*StellarBurgerLocators.PASSWORD_FIELD).send_keys(user['password'])
        driver.find_element(*StellarBurgerLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(settings.login_url))
        assert driver.current_url == settings.login_url

    def test_registration_without_name_failed(self, driver):
        driver.get(settings.registration_url)
        user = correct_user_data_generator()
        driver.find_element(*StellarBurgerLocators.EMAIL_FIELD).send_keys(user['email'])
        driver.find_element(*StellarBurgerLocators.PASSWORD_FIELD).send_keys(user['password'])
        driver.find_element(*StellarBurgerLocators.REGISTER_BUTTON).click()
        assert driver.current_url == settings.registration_url

    @pytest.mark.parametrize('email', ['ewq@.com', '22312@', '@yandex.ru', 'lskjdf2dfsf.com'])
    def test_registration_with_incorrect_email_failed(self, driver, email):
        driver.get(settings.registration_url)
        user = correct_user_data_generator()
        driver.find_element(*StellarBurgerLocators.NAME_FIELD).send_keys(user['name'])
        driver.find_element(*StellarBurgerLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*StellarBurgerLocators.PASSWORD_FIELD).send_keys(user['password'])
        driver.find_element(*StellarBurgerLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(StellarBurgerLocators.USER_ALREADY_EXIST_WARNING))
        assert expected_conditions.presence_of_element_located(StellarBurgerLocators.USER_ALREADY_EXIST_WARNING)

    @pytest.mark.parametrize('password', ['1', '3a!', '555a@'])
    def test_registration_with_short_password_failed(self, driver, password):
        driver.get(settings.registration_url)
        user = correct_user_data_generator()
        driver.find_element(*StellarBurgerLocators.NAME_FIELD).send_keys(user['name'])
        driver.find_element(*StellarBurgerLocators.EMAIL_FIELD).send_keys(user['email'])
        driver.find_element(*StellarBurgerLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*StellarBurgerLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(StellarBurgerLocators.INCORRECT_PASSWORD_WARNING))
        assert expected_conditions.presence_of_element_located(StellarBurgerLocators.INCORRECT_PASSWORD_WARNING)
