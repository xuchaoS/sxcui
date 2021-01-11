from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from sxcui.operator import Operator
from sxcui.page import Page
from sxcui.element import Locator


class BaiduPage(Page):
    # page_name = 'baidu_page'
    # search_input = Locator(By.ID, 'kw')
    # submit_button = Locator(By.ID, 'su')
    elements_path = 'baidu_page.yaml'

    def search(self, text):
        self.search_input.clear_and_input(text)
        self.submit_button.click()

    def is_active(self):
        pass


class BaiduOperator(Operator):
    def __init__(self, driver):
        super().__init__(driver)
        self.baidu_page = BaiduPage(driver)


if __name__ == '__main__':
    driver = Chrome()
    driver.get('https://www.baidu.com')
    driver.maximize_window()
    driver.implicitly_wait(30)
    operator = BaiduOperator(driver)
    operator.baidu_page.search('selenium')
    # print(operator.baidu_page.aaa)
    # operator.baidu_page
    import time

    time.sleep(1)
    operator.quit()
