from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement:

    def __init__(self, driver, selector):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.selector = selector

    def _wait_element(self):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.selector)))
