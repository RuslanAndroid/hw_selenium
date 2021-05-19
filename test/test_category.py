import pytest
from selenium.webdriver.common.by import By

from utils import assert_element


@pytest.fixture(scope="session")
def url():
    return "http://demo-opencart.ru/index.php?route=product/category&path=24"


def test_left_column(browser, url):
    browser.get(url)
    assert_element(browser, selector="#column-left")


def test_sign(browser, url):
    browser.get(url)
    assert_element(browser, selector='body > footer > div > p')


def test_products_tree(browser, url):
    browser.get(url)
    assert_element(browser, selector='#product-category > ul')


def test_cart(browser, url):
    browser.get(url)
    assert_element(browser, selector='#cart')


def test_one_item(browser, url):
    browser.get(url)
    assert_element(browser, selector='#column-left > div.swiper-viewport')
