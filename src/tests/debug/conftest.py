import pytest
from selenium import webdriver

from src.debug.core import Petclinic


@pytest.fixture(scope="session")
def browser():
    capabilities = {
        "browserName": "chrome"
    }
    driver = None
    try:
        driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=capabilities)
        driver.delete_all_cookies()
        driver.maximize_window()
    except Exception as error:
        print(error)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def petclinic(browser):
    petclinic = Petclinic(browser)
    yield petclinic
