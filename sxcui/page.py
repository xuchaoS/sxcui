from abc import ABC, abstractmethod, abstractclassmethod, abstractstaticmethod, ABCMeta, abstractproperty
from sxcui.operator import Operator


class Page(metaclass=ABCMeta):
    def __init__(self, driver):
        self.driver = driver

    def __getattr__(self, item):
        if item == 'aaa':
            return 123

    @abstractmethod
    def is_active(self):
        pass
