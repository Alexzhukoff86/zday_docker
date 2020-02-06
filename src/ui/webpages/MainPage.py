from src.helpers.ConfigReader import ConfigReader


class MainPage:

    def __init__(self, driver):
        self.__driver = driver
        self.__url = ConfigReader.get_petclinic_configs()

    def open(self):
        self.__driver.get(self.__url)
