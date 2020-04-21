from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from webwork.page.bashpage import BashPage


class ConPage(BashPage):
    def click_by_js(self, by, locator):
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element(by, locator)
                                   )
    def add_member(self, username, acctid, mail, **kwargs):
        locator = ".js_has_member .ww_operationBar .js_add_member"
        WebDriverWait(self.driver, 10, 1, ignored_exceptions=(TimeoutException)).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, locator)))

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

        self.click_by_js(By.CSS_SELECTOR,locator)
        self.driver.find_element(By.ID, 'username').send_keys(username)
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys(acctid)
        self.driver.find_element(By.ID, 'memberAdd_mail').send_keys(mail)
        self.driver.find_element(By.LINK_TEXT, '保存').click()
        return self

    def geta(self):
        pass
        return self

    def serch(self, member):
        self.driver.find_element(By.CSS_SELECTOR, '#memberSearchInput').send_keys(member)
