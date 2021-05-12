

def test_title(browser, url):
    browser.get(url)
    assert browser.title == "Opencart.ru: разработка сайтов и модулей на платформе опенкарт"
