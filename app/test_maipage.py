# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

import pytest
from appium import webdriver

from app.mainpage import MainPage
from app.myopageage import MyPage


@pytest.fixture()
def m(driver):
      a = MainPage(driver)
      yield a
      a.go_xueqiu()

# @pytest.fixture(autouse=True)
# def xueqiu(driver):
#     MainPage(driver).go_xueqiu()



class TestMain():

    def test_go_my(self, m):
        m.go_my()
        sleep(8)
    def test_go_hang(self, m):
        m.go_hangqing()
        sleep(8)

    def test_go_jiaoyi(self, m):
        m.go_jiaoyi()
        sleep(5)
