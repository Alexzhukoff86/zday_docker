from time import sleep

from src.debug.core import Petclinic


def test_find_owner(petclinic: Petclinic):
    petclinic.main_page.open()
    petclinic.main_page.open_find_owner_page()
    petclinic.find_owner_page.find_owner(last_name='Davis')

    sleep(10)