import yaml
from abc import ABC, abstractmethod, abstractclassmethod, abstractstaticmethod, ABCMeta, abstractproperty

from sxcui.element import Locator, Element
from sxcui.operator import Operator


class Page(metaclass=ABCMeta):
    elements_path = ''

    def __init__(self, driver):
        self.driver = driver
        with open(self.elements_path) as f:
            self.elements = yaml.load(f, Loader=yaml.FullLoader)

    def __getattr__(self, item):
        if item in self.elements:
            print(item)
            return Element(self.driver, self.elements[item]['by'], self.elements[item]['locator'])
        raise AttributeError(f'元素没有定义：{item}')

    @abstractmethod
    def is_active(self):
        pass
