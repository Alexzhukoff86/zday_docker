from src.ui.webpages.MainPage import MainPage


class Petclinic:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
