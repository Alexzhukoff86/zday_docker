import pytest
from selenium import webdriver

from src.core.Petclinic import Petclinic


@pytest.fixture(scope="session")
def browser():
    capabilities = {
        "browserName": "chrome"
    }
    driver = None
    try:
        driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=capabilities)
        driver.delete_all_cookies()
    except Exception as error:
        print(error)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def petclinic(browser):
    petclinic = Petclinic(browser)
    yield petclinic