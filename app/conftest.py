import pytest
from appium import webdriver
from pip._vendor.lockfile import FileLock


@pytest.fixture(scope='session')
def driver():
    # with  FileLock("session.lock"):
        caps = {}
        caps["platformName"] = "ANDROID"
        caps["deviceName"] = "seveniruby"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"
        caps['unicodeKeyboard'] = True
        driver = webdriver.Remote("http://192.168.56.1:4444/wd/hub", caps)
        driver.implicitly_wait(20)
        yield driver
        driver.quit()
