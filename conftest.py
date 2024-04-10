import pytest
import settings
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(settings.main_url)
    yield chrome_driver
    chrome_driver.quit()



