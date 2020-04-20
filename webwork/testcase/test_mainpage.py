import time

import pytest
from selenium.webdriver.common.by import By

from webwork.page.mainpage import MainPage


# @pytest.fixture(scope='module',autouse=True)
# def to(driver):
#     MainPage(driver)
# def test_to():
#     to()
class TestMain():

    # @pytest.fixture(scope='module', autouse=True)
    # def test_to(self,driver):
    #     MainPage(driver)


    def test_goto_con(self,driver):
        driver.find_element(By.LINK_TEXT, '应用管理').click()
        # MainPage(driver).goto_conpage()
        # time.sleep(10)
    def test_goto_app(self,driver):
        MainPage(driver).goto_apps()
