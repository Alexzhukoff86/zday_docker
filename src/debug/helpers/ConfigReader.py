import os


class ConfigReader:

    def __init__(self):
        pass

    @staticmethod
    def get_petclinic_configs():
        URL = "http://petclinic_demo:8080/"
        return URL