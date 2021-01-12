from selenium.webdriver.common.by import By

from sxcui.element import Element


class Locator(object):
    def __init__(self, by, locator):
        self.by = by
        self.locator = locator

    def __get__(self, instance, owner) -> Element:
        return Element(instance.driver, self.by, self.locator)


class LocatorByText(Locator):
    def __init__(self, text, tag_name='*', xpath_prefix=''):
        super().__init__(By.XPATH, f"{xpath_prefix}//{tag_name}[text()='{text}']")
