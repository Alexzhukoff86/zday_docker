from src.ui.webpages.FindOwnerPage import FindOwnerPage
from src.ui.webpages.MainPage import MainPage


class Petclinic:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.find_owner_page = FindOwnerPage(driver)
