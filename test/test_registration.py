import pytest
from selenium.webdriver.common.by import By

from utils import assert_element


@pytest.fixture(scope="session")
def url():
    return "http://demo-opencart.ru/index.php?route=account/register"


def test_hint(browser, url):
    browser.get(url)
    assert_element(browser, selector="#content > p")


def test_user_data_form(browser, url):
    browser.get(url)
    assert_element(browser, selector='#account')


def test_confirm_form(browser, url):
    browser.get(url)
    assert_element(browser, selector='#content > form > div')


def test_right_column(browser, url):
    browser.get(url)
    assert_element(browser, selector='#column-right')


def test_page_title(browser, url):
    browser.get(url)
    assert_element(browser, selector='#content > h1')
