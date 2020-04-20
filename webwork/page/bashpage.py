import time

import pytest
import yaml
from selenium.webdriver.remote.webdriver import WebDriver


class BashPage():
    def __init__(self, driver:WebDriver):
        self.driver = driver
    # def main(self):
    #     ##@pytest.fixture(scope='session', autouse=True)
    #     self.driver.delete_all_cookies()
    #     self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
    #     with open('/Users/potato/PycharmProjects/mywork/webwork/data/logincookies.yaml', 'r') as f:
    #         cookies = yaml.load(f)
    #         print(cookies)
    #
    #     for cookie in cookies:
    #         if 'expiry' in cookie:
    #             del cookie['expiry']
    #         self.driver.add_cookie(cookie)
    #     self.driver.refresh()
    #     from webwork.page.mainpage import MainPage
    #     self.driver.implicitly_wait(10)
    #     ##return MainPage(self.driver)
    # def find(self, kv) -> WebElement:
    #     # todo: 处理各类弹框
    #     return self.find(*kv)
    #
    # def find(self, by, value):
    #     element: WebElement
    #     # 加上重试机制
    #     for i in range(3):
    #         try:
    #             element = self.driver.find_element(by, value)
    #             return element
    #         except:
    #             # 找到页面的最顶层元素进行点击
    #             # 动态变化位置的元素
    #
    #             # 黑名单
    #             ##//*[@text='弹框']/..//*[@text='确认']
    #             for e in BasePage.element_black:
    #                 elements = self.driver.find_elements(*e)
    #                 if (elements.__sizeof__() > 0):
    #                     elements[0].click()
    #
    # def findByText(self, text) -> WebElement:
    #     return self.find((By.XPATH, "//*[@text='%s']" % text))
    #
    # def loadSteps(self, po_path, key, **kwargs):
    #     file = open(po_path, 'r')
    #     po_data = yaml.load(file)
    #     po_method = po_data[key]
    #     po_elements = dict()
    #     if po_data.keys().__contains__("elements"):
    #         po_elements = po_data['elements']
    #     # po_elements=yaml.load(open('xxx.yaml'))['elements']
    #
    #     for step in po_method:
    #         step: dict
    #         element_platform = dict()
    #         if step.keys().__contains__("element"):
    #             element_platform = po_elements[step['element']][AndroidClient.platform]
    #         else:
    #             element_platform = {"by": step['by'], "locator": step['locator']}
    #         element: WebElement = self.find(by=element_platform['by'], value=element_platform['locator'])
    #         action = str(step['action']).lower()
    #
    #         # todo: 定位失败，多数是弹框，try catch后进入一个弹框处理 元素智能等待
    #         if action == "click":
    #             element.click()
    #         elif action == "sendkeys":
    #             text = str(step['text'])
    #             for k, v in kwargs.items():
    #                 origin = text
    #                 text = text.replace("$%s" % k, v)
    #                 print("update text: %s %s" % (origin, text))
    #             element.send_keys(text)
    #         else:
    #             print("UNKNOW COMMAND %s" % step)
