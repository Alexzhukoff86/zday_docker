from selenium import webdriver

from source.pages.MainPage import MainPage


def test_firefox():
    capabilities = {
        "browserName": "firefox"
    }
    firefox = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=capabilities)
    firefox.maximize_window()

    main_page = MainPage(firefox)
    main_page.open().click_with_us_button()
    firefox.get_screenshot_as_file('screenshot_firefox.png')

    firefox.quit()
