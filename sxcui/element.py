from selenium.webdriver.remote.webdriver import WebDriver


class Element(object):
    def __init__(self, driver: WebDriver, by, locator):
        self.driver = driver
        self.by = by
        self.locator = locator
        self.element = driver.find_element(by, locator)

    def click(self):
        self.element.click()

    def input(self, text):
        self.element.clear()
        self.element.send_keys(text)


class Locator(object):
    def __init__(self, by, locator):
        self.by = by
        self.locator = locator

    def __get__(self, instance, owner) -> Element:
        return Element(instance.driver, self.by, self.locator)
