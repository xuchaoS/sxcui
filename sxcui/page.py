from abc import ABC, abstractmethod, abstractclassmethod, abstractstaticmethod, ABCMeta, abstractproperty
from sxcui.operator import Operator


class RegisterPage(object):
    def __init__(self, cls: type):
        self.cls = cls

    def __get__(self, instance, owner):
        return self.cls(instance.driver)


class Page(metaclass=ABCMeta):
    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def is_active(self):
        pass
