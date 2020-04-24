import time

from commont.commont import Commont
from webwork.commnt import *
import pytest
import yaml
from selenium.webdriver.remote.webdriver import WebDriver


class BashPage(Commont):
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def loadSteps(self, po_path, key, **kwargs):
        file = open(po_path, 'r', encoding='utf_8')
        po_data = yaml.load(file)
        po_method = po_data[key]
        # po_elements = dict()
        # if po_data.keys().__contains__("elements"):
        #     po_elements = po_data['elements']
        # # po_elements=yaml.load(open('xxx.yaml'))['elements']

        for step in po_method:
            ##step: dict
            ##element_platform = dict()
            # if step.keys().__contains__("element"):
            #     element_platform = po_elements[step['element']]
            # else:
           ## element_platform = {"by": step['by'], "locator": step['locla']}
            element: WebElement = find(self.driver, by=step['by'], value=step['locla'])
            action = str(step['action']).lower()

            # todo: 定位失败，多数是弹框，try catch后进入一个弹框处理 元素智能等待
            if action == "click":
                element.click()
            elif action == "sendkeys":
                text = str(step['text'])
                for k, v in kwargs.items():
                    origin = text
                    text = text.replace("$%s" % k, v)
                    print("update text: %s %s" % (origin, text))
                element.send_keys(text)
            else:
                print("UNKNOW COMMAND %s" % step)