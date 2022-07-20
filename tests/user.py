import pytest, time

from typing import Callable

from urllib import parse
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webdriver
from selenium.webdriver.remote import webelement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture(scope='session')
def browser_user(selenium_driver):
    yield BrowserUser(selenium_driver)


class BrowserUser:

    def __init__(self, driver: webdriver.WebDriver) -> None:
        self.driver = driver
        self.trusted_cookies_domain = set()

    def browse(self, url: str, trust_cookies_func: Callable[[], None]) -> str:
        self.driver.get(url)

        domain = parse.urlparse(url).netloc
        if domain not in self.trusted_cookies_domain:
            trust_cookies_func()
            self.trusted_cookies_domain.add(domain)

    def wait_to_see_webpage_url(self, url: str, timeout_seconds: int) -> bool:
        try:
            return WebDriverWait(self.driver, timeout_seconds).until(
                expected_conditions.url_to_be(url)
            )
        except TimeoutException:
            return False

    def locate_elements(self, xpath: str) -> list[webelement.WebElement]:
        return self.driver.find_elements(By.XPATH, xpath)

    def locate_element(self, xpath: str) -> webelement.WebElement:
        elements = self.locate_elements(xpath)
        if elements:
            if len(elements) > 1:
                raise Exception(f"User unable to determine which element to click. Got `{elements}` for xpath `{xpath}`")
            return elements[0]
        else:
            raise Exception(f"User unable to find xpath `{xpath}` to click")

    def click(self, xpath: str):
        self.locate_element(xpath).click()

    def see_element_text(self, xpath: str) -> str:
        return self.locate_element(xpath).text 

    def see_element_value(self, xpath: str) -> str:
        return self.locate_element(xpath).get_attribute("value") 

    def hover_over(self, xpath: str) -> webelement.WebElement:
        element = self.locate_element(xpath)
        ActionChains(self.driver).move_to_element(element).perform()

    def see_element_css_property(self, xpath: str, css_property: str) -> str:
        return self.locate_element(xpath).value_of_css_property(css_property)

    def fill_in_input_value(self, xpath: str, fill_in_value: str) -> str:
        self.locate_element(xpath).send_keys(fill_in_value)

    def wait_to_get_elements(self, xpath: str, timeout_seconds: int) -> list[webelement.WebElement]:
        try:
            return WebDriverWait(self.driver, timeout_seconds).until(
                expected_conditions.presence_of_all_elements_located((By.XPATH, xpath))
            )
        except TimeoutException:
            return []

    def wait_to_get_element(self, xpath: str, timeout_seconds: int) -> webelement.WebElement:
        elements = self.wait_to_get_elements(xpath, timeout_seconds)
        if elements:
            if len(elements) > 1:
                raise Exception(f"User unable to determine which element to click. Got `{elements}` for xpath `{xpath}`")
            return elements[0]
        else:
            raise Exception(f"User unable to find xpath `{xpath}` to click")

    def wait_element_clickable(self, xpath: str, timeout_seconds: int) -> bool:
        try:
            if element := self.wait_to_get_element(xpath, timeout_seconds):
                if element := WebDriverWait(self.driver, timeout_seconds).until(
                        expected_conditions.element_to_be_clickable(element)
                    ):
                    return True
            return False
        except TimeoutException:
            return False

    def wait_to_see_element_contain_text(self, xpath: str, expect_text: str, timeout_seconds: int) -> bool:
        try:
            return WebDriverWait(self.driver, timeout_seconds).until(
                expected_conditions.text_to_be_present_in_element((By.XPATH, xpath), expect_text)
            )
        except TimeoutException:
            return False

    def wait_until_element_invisible(self, xpath: str, timeout_seconds: int) -> bool:
        try:
            if WebDriverWait(self.driver, timeout_seconds).until(
                    expected_conditions.invisibility_of_element_located((By.XPATH, xpath))
                ):
                return True
            return False
        except TimeoutException:
            return False
