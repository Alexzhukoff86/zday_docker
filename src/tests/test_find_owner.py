from time import sleep

from src.core.Petclinic import Petclinic


def test_find_owner(petclinic: Petclinic):
    petclinic.main_page.open()
    sleep(10)