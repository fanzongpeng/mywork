from selenium.webdriver.common.by import By

from app.bashpage import BashPage
from app.hangpage import HangPage
from app.jiaoyipage import JiaoPage
from app.myopageage import MyPage
from app.searchpage import SearchPage
from app.xuepage import XuePage


class MainPage(BashPage):
    def go_search(self):
        self.driver.find_element(By.ID, 'tv_search').click()
        return SearchPage(self.driver)

    def go_my(self):
        self.driver.find_element(By.XPATH, "//*[@text='我的']").click()
        return MyPage(self.driver)

    def go_hangqing(self):
        self.driver.find_element(By.XPATH, "//*[@text='行情']").click()
        return HangPage(self.driver)
    def go_jiaoyi(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易']").click()
        return JiaoPage(self.driver)
    def go_xueqiu(self):
        self.driver.find_element(By.XPATH, "//*[@text='雪球']").click()
        return XuePage(self.driver)










