from abc import ABC, abstractmethod, abstractclassmethod, abstractstaticmethod, ABCMeta, abstractproperty
from sxcui.operator import Operator


class PageMeta(type):
    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        if name != 'Page':
            Operator.pages[name] = cls
            page_name = namespace.get('page_name', '')
            if page_name:
                Operator.pages[page_name] = cls
        return cls


class Page(metaclass=PageMeta):
    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def is_active(self):
        pass
