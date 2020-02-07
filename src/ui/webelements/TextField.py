from selenium.webdriver.common.by import By

from src.ui.webelements.BaseElement import BaseElement


class TextField(BaseElement):

    def __init__(self, driver, selector):
        super().__init__(driver, selector)
        self.element = self.driver.find_element(By.XPATH, self.selector)

    def enter_value(self, text):
        super()._wait_element()
        self._clear_field()
        self.element.send_key(text)

    def _clear_field(self):
        super()._wait_element()
        self.element.clear()