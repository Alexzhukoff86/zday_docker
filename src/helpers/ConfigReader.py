import os


class ConfigReader:

    def __init__(self):
        pass

    @staticmethod
    def get_petclinic_configs():
        URL = "http://172.25.0.5:8080/"
        return URL