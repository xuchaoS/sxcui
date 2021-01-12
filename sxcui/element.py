import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException


class Element(object):
    def __init__(self, driver: WebDriver, by, locator, delay=10):
        self.driver = driver
        self.by = by
        self.locator = locator
        self.delay = delay
        self.element = driver.find_element(by, locator)

    def click(self):
        start_time = time.time()
        WebDriverWait(self.driver, self.delay).until(
            ec.element_to_be_clickable((self.by, self.locator))
        )
        while time.time() - start_time > self.delay:
            try:
                self.element.click()
                break
            except ElementClickInterceptedException:
                time.sleep(0.1)

    @property
    def text(self):
        WebDriverWait(self.driver, self.delay).until(
            ec.visibility_of(self.element)
        )
        return self.element.text

    def input(self, text):
        self.element.send_keys(text)

    def clear(self):
        self.element.clear()

    def clear_and_input(self, text):
        self.clear()
        self.input(text)

    @property
    def text_of_input(self):
        return self.element.get_attribute('value')

    def _get_next_element(self, xpath_locator):
        if self.by != By.XPATH:
            raise Exception('调用查找下一个元素，需要原始定位为XPATH方式')
        return self.__class__(
            self.driver,
            By.XPATH,
            f"{self.locator}/following::{xpath_locator.strip('/')}"
        )

    @property
    def _next_input(self):
        return self._get_next_element('input')

    @property
    def _next_button(self):
        return self._get_next_element('button')

    def input_next_input(self, text):
        self._next_input.input(text)

    def clear_next_input(self):
        self._next_input.clear()

    def clear_and_input_next_input(self, text):
        self._next_input.clear_and_input(text)
