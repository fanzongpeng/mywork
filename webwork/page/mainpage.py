import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from webwork.page.appspage import AppsPage
from webwork.page.bashpage import BashPage
from webwork.page.conpage import ConPage


class MainPage(BashPage):
    # def __init__(self,driver:WebDriver):
    #     self.driver=driver
    def goto_conpage(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.LINK_TEXT, '通讯录').click()
        return ConPage(self.driver)
    def goto_apps(self):
        self.driver.find_element(By.LINK_TEXT, '应用管理').click()
        return AppsPage(self.driver)
