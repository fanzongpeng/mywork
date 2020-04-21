import pytest

from webwork.page.mainpage import MainPage


class TestApps():
    @pytest.fixture(scope='module',autouse=True)
    def app(self,driver):
        MainPage(driver).goto_apps()
    def test1(self,driver):
        pass
    def test2(self):
        pass