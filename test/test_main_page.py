import pytest
from selenium.webdriver.common.by import By

from utils import assert_element


@pytest.fixture(scope="session")
def url():
    return "http://demo-opencart.ru/index.php"


def test_menu(browser, url):
    browser.get(url)
    assert_element(browser, selector="navbar", selector_type=By.CLASS_NAME)


def test_banners(browser, url):
    browser.get(url)
    assert_element(browser, selector="swiper-viewport", selector_type=By.CLASS_NAME)


def test_carusel(browser, url):
    browser.get(url)
    assert_element(browser, selector="#carousel0")


def test_footer(browser, url):
    browser.get(url)
    assert_element(browser, selector="body > footer")


def test_search(browser, url):
    browser.get(url)
    assert_element(browser, selector="#search")
