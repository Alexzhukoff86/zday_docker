from selenium import webdriver
from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver: webdriver):
        self.__driver = driver

    def open(self):
        self.__driver.get('https://www.zfort.com/')
        return self

    def click_with_us_button(self):
        self._with_us = self.__driver.find_element(By.XPATH, MainPageLocators.WORK_WITH_US)
        self._with_us.click()


class MainPageLocators:
    WORK_WITH_US = "//div[@class='visual--frame']//a[@class='btn-basic']"
