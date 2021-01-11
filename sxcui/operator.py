from abc import ABCMeta, abstractmethod
from selenium.webdriver.remote.webdriver import WebDriver


class Operator(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def quit(self):
        self.driver.quit()
