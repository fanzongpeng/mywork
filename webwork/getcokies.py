import time

import pytest
import yaml
from selenium import webdriver


def getcookies():
    driver = webdriver.Chrome(
        executable_path='/usr/local/bin/chromdriver')
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
    bef = driver.get_cookies()
    print("+++++++++" + str(bef))
    print(len(bef))
    time.sleep(10)
    cookies = driver.get_cookies()
    print("___________" + str(cookies))
    print(len(cookies))

    with open("/Users/potato/PycharmProjects/mywork/data/logincookies.yaml", "w") as f:
        yaml.dump(cookies, f)


getcookies()
