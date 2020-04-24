import allure
import pytest
from selenium.webdriver.common.by import By

from webwork.commnt import read_yaml
from webwork.page.mainpage import MainPage


@pytest.fixture(scope='class')
def con(login):
    con = login.goto_conpage()
    return con


@allure.feature('通讯录功能测试')
class TestCon():
    # @pytest.fixture(scope='class',autouse=True)
    # def com(self):
    #      MainPage().goto_conpage()
    @allure.story('添加成员正向测试')
    def test_addmember(self, con):
        con.add_member("李-袋", '9527424800000', '423658119@qq.com')

        # login.goto_conpage().add_member("李袋", '95274248000', '4238472389@qq.com')

    @pytest.mark.parametrize(('username', 'acctid', 'mail', 'msg'), [('李晓', '94305435@qq.com', '', '手机和邮箱不能同事为空')])
    def test_add_by(self, con, username, acctid, mail, msg):
        con.add_member(username, acctid, mail)
        assert msg == con.msgemail()
