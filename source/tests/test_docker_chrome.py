from time import sleep

from selenium import webdriver

from source.pages.MainPage import MainPage


def test_chrome():
    capabilities = {
        "browserName": "chrome"
    }
    chrome = webdriver.Remote(command_executor='http://hub:4444/wd/hub', desired_capabilities=capabilities)
    chrome.maximize_window()

    main_page = MainPage(chrome)
    main_page.open().click_with_us_button()
    chrome.get_screenshot_as_file('screenshot_chrome_docker.png')
    sleep(2)

    chrome.close()
    chrome.quit()
