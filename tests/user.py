import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webdriver


@pytest.fixture(scope='session')
def browser_user(selenium_driver):
    yield BrowserUser(selenium_driver)


class BrowserUser:

    def __init__(self, driver: webdriver.WebDriver) -> None:
        self.driver = driver

    def browse(self, url: str) -> str:
        self.driver.get(url)
        self
        import time
        time.sleep(10)

    def see_webpage_url(self) -> str:
        return self.driver.current_url

    def click(self, xpath: str):
        results = self.driver.find_elements(By.XPATH, xpath)
        if results:
            if len(results) > 1:
                raise Exception(f"User unable to determine which element to click. Got `{results}` for xpath `{xpath}`")
            results[0].click()
        else:
            raise Exception(f"User unable to find xpath `{xpath}` to click")

    def see_text_on_element(self, xpath_element: str) -> str:
        return 