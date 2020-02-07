from src.ui.webelements.TextField import TextField
from src.ui.webpages.BasePage import BasePage


class FindOwnerPageLocators:
    LAST_NAME_FLD = "//input[@id='lastName']"
    FIND_OWNER_BTN = "//button[@class='btn btn-default']"
    ADD_OWNER_BTN = ""


class FindOwnerPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def find_owner(self, last_name):
        self._last_name = TextField(driver=self.driver, selector= FindOwnerPageLocators.FIND_OWNER_BTN)
        self._last_name.enter_value(last_name)
        
