import pytest
from selenium.webdriver.common.by import By

from utils import assert_element


@pytest.fixture(scope="session")
def url():
    return "http://demo-opencart.ru/index.php?route=information/contact"


def test_contacts(browser, url):
    browser.get(url)
    assert_element(browser, selector="#content > div.panel.panel-default")


def test_shops_list(browser, url):
    browser.get(url)
    assert_element(browser, selector='#accordion')


def test_contact_form(browser, url):
    browser.get(url)
    assert_element(browser, selector='#content > form > fieldset')


def test_send_message_btn(browser, url):
    browser.get(url)
    assert_element(browser, selector='#content > form > div')


def test_page_title(browser, url):
    browser.get(url)
    assert_element(browser, selector='#content > h1')
