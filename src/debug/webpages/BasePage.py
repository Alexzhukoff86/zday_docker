from src.helpers.ConfigReader import ConfigReader


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(ConfigReader.get_petclinic_configs())
        return self
