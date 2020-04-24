from time import sleep
from webwork.commnt import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from webwork.page.bashpage import BashPage


class ConPage(BashPage):
    _username = (By.ID, 'username')

    # def click_by_js(self, by, locator):
    #     self.driver.execute_script("arguments[0].click();",
    #                                self.driver.find_element(by, locator)
    #                                )

    # def find(self, by, ele):
    #     element = self.driver.find_element(by, ele)
    #     return element

    def add_member(self, username, acctid, mail, **kwargs):
        locator = '.js_has_member .ww_operationBar .js_add_member'
        # WebDriverWait(self.driver, 10, 1, ignored_exceptions=(TimeoutException)).until(
        #     expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, locator)))
        wait_click(self.driver, By.CSS_SELECTOR, locator)

        # for index in range(10):
        #     element = self.driver.find_element_by_css_selector(locator)
        #     print(element.rect)
        #     print(element.text)
        #     print(element.tag_name)
        #     sleep(0.5)
        #
        # print(self.driver.page_source)
        # #todo: 找到等待的状态
        # sleep(3)
        # print("3s")
        # for index in range(10):
        #     print(self.driver.find_element_by_css_selector(locator).location)
        #     sleep(0.5)

        click_by_js(self.driver, By.CSS_SELECTOR, locator)
        ## self.find(By.ID, 'username').send_keys(username)
        # find_ele(self.driver, self._username).send_keys(username)
        #
        # self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys(acctid)
        # self.driver.find_element(By.ID, 'memberAdd_mail').send_keys(mail)
        # self.driver.find_element(By.LINK_TEXT, '保存').click()
        filepath = '/Users/potato/PycharmProjects/mywork/data/com.yaml'
        self.loadSteps(filepath, 'add_member', var1=username, var2=acctid, var3=mail)
        return self

    def msgemail(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="js_contacts36"]'
                                                 '/div/div[2]/div/div[4]/div/form/div[2]/div[2]/div[1]/div/div[2]')
        msg = ele.text
        print(type(msg), msg)
        return msg

    def geta(self):
        pass
        return self

    def serch(self, member):
        self.driver.find_element(By.CSS_SELECTOR, '#memberSearchInput').send_keys(member)
