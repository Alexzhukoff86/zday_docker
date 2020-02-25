from src.helpers.ConfigReader import ConfigReader
from src.ui.webelements.Button import Button
from src.ui.webpages.BasePage import BasePage

class MainPageLocators:

    FIND_OWNER_BTN = "//*[@title='find owners']"


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    def open_find_owner_page(self):
        self._find_owner_button = Button(driver=self.driver, selector=MainPageLocators.FIND_OWNER_BTN)
        self._find_owner_button.click()
        return self



    #locators
    __home_page_btn = ""
    __find_owner_btn="//*[@title='find owners']"
    __veterinars_btn=""
