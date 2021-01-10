from typing import Iterable

from selenium.webdriver.remote.webdriver import WebDriver


class Operator(object):
    pages = {}

    def __init__(self, driver: WebDriver):
        self.driver = driver
        for k, v in self.pages.items():
            self.__dict__[k] = v(self.driver)

    def __getattr__(self, item):
        if item in self.pages:
            return self.pages[item](self.driver)
        raise AttributeError(f'{self.__class__.__name__}中不存在{item}')

    def __dir__(self) -> Iterable[str]:
        return self.pages.keys()

    def quit(self):
        self.driver.quit()


