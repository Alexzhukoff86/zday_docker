from selenium import webdriver
from selenium.webdriver.common.by import By

from src.ui.webelements.BaseElement import BaseElement


class Button(BaseElement):

    def __init__(self, driver, selector):
        super().__init__(driver, selector)
        self.element = self.driver.find_element(By.XPATH, self.selector)

    def click(self):
        super()._wait_element()
        self.element.click()
