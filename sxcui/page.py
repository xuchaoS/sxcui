import yaml
import json
import csv
from abc import ABC, abstractmethod, abstractclassmethod, abstractstaticmethod, ABCMeta, abstractproperty

from sxcui.element import Locator, Element
from sxcui.operator import Operator


class Page(metaclass=ABCMeta):
    elements_path = ''

    def __init__(self, driver):
        self.driver = driver
        if self.elements_path.endswith('yaml'):
            with open(self.elements_path) as f:
                self.elements = yaml.load(f, Loader=yaml.FullLoader)
        elif self.elements_path.endswith('json'):
            with open(self.elements_path) as f:
                self.elements = json.load(f)
        elif self.elements_path.endswith('csv'):
            with open(self.elements_path) as f:
                reader = csv.DictReader(f)
                self.elements = {}
                for row in reader:
                    self.elements[row['name']] = row
            
    def __getattr__(self, item):
        if item in self.elements:
            print(item)
            return Element(self.driver, self.elements[item]['by'], self.elements[item]['locator'])
        raise AttributeError(f'元素没有定义：{item}')

    @abstractmethod
    def is_active(self):
        pass
