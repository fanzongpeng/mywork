import pytest
from appium import webdriver
from pip._vendor.lockfile import FileLock

##pytest-xdist是让每个worker进程执行属于自己的测试用例集下的所有测试用例

##这意味着在不同进程中，不同的测试用例可能会调用同一个scope范围级别较高（例如session）的fixture，该fixture则会被执行多次，这不符合scope=session的预期
# 下面的示例只需要执行一次login（因为它是只需要执行一次来定义配置选项，等等）
# 当第一次请求这个fixture时，则会利用FileLock仅产生一次fixture数据
# 当其他进程再次请求这个fixture时，则会从文件中读取数据
@pytest.fixture(scope='session')
def driver():
    with  FileLock("session.lock"):

        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "seveniruby"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"
        caps['unicodeKeyboard'] = True

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
    return driver
