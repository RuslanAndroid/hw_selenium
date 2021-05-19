import pytest
import os
from selenium import webdriver
from selenium.webdriver.opera.options import Options as OperaOptions

DRIVERS = os.path.expanduser("~/Downloads/drivers")


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://www.opencart.ru/", help="Адрес сайта")
    parser.addoption("--big_screen", action="store_true", help="На весь экран")
    parser.addoption("--hide", action="store_true", help="Скрытый режим")
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera"],
                     default="chrome", help="Можно указать браузер")
@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")

@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption("--browser")
    hide = request.config.getoption("--hide")
    big_screen = request.config.getoption("--big_screen")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.headless = hide
        driver = webdriver.Chrome(options=options, executable_path=f"{DRIVERS}/chromedriver")
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.headless = hide

        driver = webdriver.Firefox(
            options=options,
            executable_path=f"{DRIVERS}/geckodriver"
        )
    elif browser == "opera":
        options = OperaOptions()

        driver = webdriver.Opera(
            options=options,
            executable_path=f"{DRIVERS}/operadriver"
        )
    else:
        raise ValueError("Driver not supported: {}".format(browser))

    request.addfinalizer(driver.quit)

    if big_screen:
        driver.maximize_window()

    return driver
