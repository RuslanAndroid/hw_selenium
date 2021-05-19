from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def assert_element(driver, selector, timeout=1, selector_type=By.CSS_SELECTOR):
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((selector_type, selector)))
    except TimeoutException:
        # Перехватываем исключение и атачим скриншот
        driver.save_screenshot("{}.png".format(driver.session_id))
        # Выбрасываем AssertionError
        raise AssertionError("Не дождался видимости элемента: {}".format(selector))
