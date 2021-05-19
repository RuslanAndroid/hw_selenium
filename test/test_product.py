from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utils import assert_element

url = "http://demo-opencart.ru/index.php?route=product/product&product_id=43"


def test_buy_button(browser):
    browser.get(url)
    assert_element(browser, selector='#button-cart')


def test_logo(browser):
    browser.get(url)
    assert_element(browser, selector="#logo")


def test_desc_content(browser):
    browser.get(url)
    assert_element(browser, selector="tab-content", selector_type=By.CLASS_NAME)


def test_rating(browser):
    browser.get(url)
    assert_element(browser, selector="rating", selector_type=By.CLASS_NAME)


def test_bchange_language(browser):
    browser.get(url)
    assert_element(browser, selector="#form-language > div > button")
