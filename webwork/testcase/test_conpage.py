import allure

from webwork.page.mainpage import MainPage


@allure.feature('通讯录功能测试')
class TestCon():
    @allure.story('添加成员正向测试')
    def test_addmember(self, login):
        login.goto_conpage().add_member("李小袋", '952742489', '4238472389@qq.com')

    def test_add_by(self,login):
        login.goto_conpage().add_member("李小袋", '952742489', '')
