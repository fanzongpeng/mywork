from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import pytest

from webwork.page.bashpage import BashPage


class ConPage(BashPage):
    ##添加成员
    # def __init__(self,driver:WebDriver):
    #     self.driver=driver
    # @pytest.fixture(scope='class',autouse=True)
    # def co(self,login):
    #     pass




    def add_member(self):
        self.driver
        self.driver.find_element(By.CSS_SELECTOR,'.js_has_member > div:nth-child(1) > a.qui_btn.ww_btn.js_add_member').click()
        ##self.driver.find_element()

        return self


