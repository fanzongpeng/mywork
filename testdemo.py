import os
import time
from threading import Thread

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.remote.webelement import WebElement

from commont.commont import Commont
from webwork.commnt import *


class TestDemo(Commont):
    def test_read_yaml(self):
        filepath = '/Users/potato/PycharmProjects/mywork/data/com.yaml'
        with open(filepath, 'r', encoding='utf_8') as f:
            data = yaml.load(f)
            print(data)
        for v in data['add_member']:
            webdriver.Remote()
            chromoption = webdriver.ChromeOptions()
            print(v)

    def loadSteps(self, po_path, key, **kwargs):
        file = open(po_path, 'r', encoding='utf_8')
        po_data = yaml.load(file)
        po_method = po_data[key]
        # po_elements = dict()
        # if po_data.keys().__contains__("elements"):
        #     po_elements = po_data['elements']
        # # po_elements=yaml.load(open('xxx.yaml'))['elements']

        for step in po_method:
            step: dict
            ##element_platform = dict()
            # if step.keys().__contains__("element"):
            #     element_platform = po_elements[step['element']]
            # else:
            element_platform = {"by": step['by'], "locator": step['locator']}
            element: WebElement = wait_click(self.driver, by=element_platform['by'], value=element_platform['locator'])
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

    def test1(self, host, browser):

        self.driver = webdriver.Remote(
            command_executor=host,
            # desired_capabilities=DesiredCapabilities.,
            desired_capabilities={'platform': 'ANY', 'browserName': browser, 'version': '',
                                  'javascriptEnabled': True}
        )
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
        wait_click(self.driver, By.LINK_TEXT, '通讯录')
        click_by_js(self.driver, By.LINK_TEXT, '通讯录')
        # wait_click(self.driver, By.CSS_SELECTOR, '.js_has_member .ww_operationBar .js_add_member')
        # click_by_js(self.driver, By.CSS_SELECTOR, '.js_has_member .ww_operationBar .js_add_member')
        # find(self.driver, By.ID, 'username').send_keys('3463tb4g')
        #
        # self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys('190823nhb')
        # self.driver.find_element(By.ID, 'memberAdd_mail').send_keys('98765@qq.com')
        # click_by_js(self.driver, By.CSS_SELECTOR, '.js_member_editor_form > div:nth-child(3)>.js_btn_save')
        # ## self.driver.find_element(By.CSS_SELECTOR, '.js_member_editor_form > div:nth-child(3)>.js_btn_save').click()
        #
        # time.sleep(5)
        self.driver.quit()

    ##多线程
    def test2(self):
        nodes = {"http://127.0.0.1:5555/wd/hub": 'safari',
                 "http://127.0.0.1:5556/wd/hub": 'chrome'
                 }

        threads = []
        files = range(len(nodes))

        # 创建线程
        for host, browser in nodes.items():
            t = Thread(target=self.test1, args=(host, browser))
            threads.append(t)

        # 启动线程
        for i in files:
            threads[i].start()
        for i in files:
            threads[i].join()

    def test_wyaml(self):
        file = {'add_member': [{'locla': 'username', 'by': 'id', 'action': 'sendKeys', 'text': '$var1'},
                               {'locla': 'memberAdd_acctid', 'by': 'id', 'action': 'sendKeys', 'text': '$var2'},
                               {'locla': 'memberAdd_mail', 'by': 'id', 'action': 'sendKeys', 'text': '$var3'},
                               {'locla': '.js_member_editor_form > div:nth-child(3)>.js_btn_save', 'by': 'CSS_SELECTOR',
                                'action': 'click'}]}
        with open('/Users/potato/PycharmProjects/mywork/data/w.yaml', 'w', encoding='utf-8') as f:
            data = yaml.dump(file, f)
            print(data)

    # def test2(self):
    #     def decor(func):
    #         def wrap():
    #             print("============")
    #             func()
    #             print("============")
    #
    #         return wrap
    #
    #     @decor
    #     def print_text():
    #         print("Hello world!")
    def test6(self):

        from selenium.webdriver import Remote
        import time

        # 定义node_hub与浏览器对应关系
        nodes = {
            'http://127.0.0.1:5556/wd/hub': 'firefox',
            'http://127.0.0.1:5555/wd/hub': 'internet explorer',
            ##'http://127.0.0.1:5557/wd/hub': 'chrom'
        }

        # 通过不同的浏览器执行测试脚本
        for host, browser in nodes.items():
            print(host, browser)
            # 调用remote方法
            self.driver = Remote(command_executor=host,
                                 desired_capabilities={'platform': 'ANY', 'browserName': browser, 'version': '',
                                                       'javascriptEnabled': True})

            # 打开百度首页并搜索词语，最后判断搜索跳转页面标题是否含有搜索词
            wd = 'lovesoo'
            self.driver.get('https://www.baidu.com')
            self.driver.find_element_by_id("kw").send_keys(wd)
            self.driver.find_element_by_id("su").click()
            time.sleep(1)
            assert wd in self.driver.title, '{0} not in {1}'.format(wd, self.driver.title.encode('utf-8'))
            self.driver.quit()

        # # 浏览器数组
        # lists = ['chrome', 'internet explorer', 'firefox']
        # # 通过不同的浏览器执行脚本
        # for browser in lists:
        #     driver = webdriver.Remote(
        #         command_executor='http://127.0.0.1:4444/wd/hub',
        #         desired_capabilities={'platform': 'ANY',
        #                               'browserName': browser,
        #                               'version': '',
        #                               'javascriptEnabled': True
        #                               })

    def test4(self):
        self.driver = webdriver.Remote(
            command_executor="http://127.0.0.1:5555/wd/hub",
            # desired_capabilities=DesiredCapabilities.,
            desired_capabilities={'platform': 'ANY', 'browserName': 'chrome', 'version': '',
                                  'javascriptEnabled': True}
        )
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com')
        handle1 = self.get_handle()
        self.find(By.LINK_TEXT, '新闻').click()
        self.switch_window(handle1)
        self.driver.implicitly_wait(5)
        a = self.find_scro(By.XPATH, '//*[@id="footerwrapper"]/div[1]/div/div[1]/div[1]/h4').text
        print(a)
        time.sleep(5)
        self.driver.quit()

    def test_path(self):
        b = self.file_path('data/com.yaml')
        # a=os.path.dirname(os.path.realpath(__file__))
        # b=os.path.join(a,'data/com.yaml')
        self.read_yaml(b)

    def test_excel(self):
        b = self.file_path('data/cases.xlsx')
        c = self.get_excel_data(b,'用例','登陆')
        print(c)
