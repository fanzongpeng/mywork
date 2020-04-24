import csv
from unittest.mock import ANY

import yaml
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Commont():
    driver: WebDriver

    ##定位元素
    def find(self, by, value) -> WebElement:
        element = self.driver.find_element(by, value)
        print(element)
        return element

    ##定位元素
    def find_value(self, value) -> WebElement:
        element = self.driver.find_element(*value)
        print(element)
        return element

    ##等待元素可点击状态
    def wait_click(self, by, value) -> WebElement:
        element = WebDriverWait(self.driver, 10, 1, ignored_exceptions=(TimeoutException)) \
            .until(expected_conditions.element_to_be_clickable((by, value)))
        return element

    ## js点击元素
    def click_by_js(self, by, value):
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element(by, value))

    ##等待元素可见
    def wait_see(self, by, value) -> WebElement:
        element = WebDriverWait(self.driver, 10, 1, ignored_exceptions=(TimeoutException)).until(
            expected_conditions.visibility_of_element_located((by, value)))
        return element

    ##等待元素消失
    def wait_no(self, by, value) -> WebElement:
        element = WebDriverWait(self.driver, 10, 1, ignored_exceptions=(TimeoutException)).until(
            expected_conditions.invisibility_of_element_located((by, value)))
        return element

    ##向下滑动到元素位置
    def find_scro(self, by, value) -> WebElement:
        element = self.driver.find_element(by, value)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
        return element

    # 向上滑动滚动条，跳转到目标元素处
    def find_by_js(self, by, value) -> WebElement:
        element = self.driver.driver.find_element(by, value)
        self.driver.execute_script('arguments[0].scrollIntoView(false);', element)
        return element
##获取窗口手柄
    def get_handle(self):
        handle = self.driver.current_window_handle
        return handle

    ##切换窗口
    def switch_window(self, handle1):
        # 等待有两个窗口
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))
        # Loop through until we find a new window handle
        for window_handle in self.driver.window_handles:
            if window_handle != handle1:
                self.driver.switch_to.window(window_handle)

    ##判断弹窗
    def switch_alert(self):
        # Wait for the alert to be displayed
        self.wait.until(expected_conditions.alert_is_present())
        # Store the alert in a variable for reuse
        alert = self.driver.switch_to.alert
        # Store the alert text in a variable
        text = alert.text

        # Press the Cancel button

    ##页面加载策略    alert.dismiss()
    def jiazai(self):
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.page_load_strategy = 'normal'
        driver = webdriver.Chrome(options=options)
        # Navigate to url
        driver.get("http://www.google.com")
        driver.quit()

    ##切换frame  frameset不用切 ，iframe和frame需要切换(id,name,下标，元素定位)

    def switch_frame(self, search: ANY):
        self.driver.switch_to.frame(search)
        return self

    ##切换到 主页面主文档 frame
    def switch_defaule(self):
        self.driver.switch_to.default_content()
        return self

    # 切换到主frame
    def switch_parent_frame(self):
        self.driver.switch_to.parent_frame()

        return self
  ##读取yanml文件
    def read_yaml(self,filepath):
        with open(filepath,'r') as f:
            data=yaml.load(f)
        return data
    def writ_yaml(self,filepath,data):
        with open(filepath,'w') as f:
            yaml.dump(data,f)

    def read_excel(self,filepath):
        with open(filepath,'r') as f:

            pass
    def read_txt(self,filepath):
        with open(filepath,'r') as f:
            data=f.read()
        return data
    def read_csv(self,filepath):
        with open(filepath,'r') as f:
            data=csv.reader(f)
        return csv



