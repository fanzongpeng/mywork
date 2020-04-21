import time

import pytest
import yaml
from selenium import webdriver


@pytest.fixture(scope="session", autouse=True)
def driver():
    driver = webdriver.Chrome(
        executable_path='/usr/local/bin/chromdriver')
    driver.implicitly_wait(5)
    driver.maximize_window()
    # yield driver
    return driver
    # driver.quit()


@pytest.fixture(scope='session', autouse=True)
def login(driver):
    driver.delete_all_cookies()
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')


    with open('/Users/potato/PycharmProjects/mywork/data/logincookies.yaml', 'r') as f:
        cookies = yaml.load(f)
        print(cookies)

    for cookie in cookies:
        if 'expiry' in cookie:
            del cookie['expiry']
        driver.add_cookie(cookie)
        ## driver.refresh()
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')

    from webwork.page.mainpage import MainPage

    driver.implicitly_wait(10)
    return MainPage(driver)
