import time

import allure
import pytest
from selenium.webdriver.common.by import By

from webwork.page.mainpage import MainPage


# @pytest.fixture(scope='module',autouse=True)
# def to(driver):
#     MainPage(driver)
# def test_to():
#     to()
# @pytest.fixture(scope='class',autouse=True)
# def main(driver):
#     return MainPage(driver)
@allure.feature('首页测试')
class TestMain():


    @allure.story('点击去通讯录页面测试')
    def test_goto_con(self,driver,login):

        login.goto_conpage()
        time.sleep(10)
    @allure.story('点击去应用管理页面')
    def test_goto_app(self,driver,login):
        login.goto_apps()
        time.sleep(5)
