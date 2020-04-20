import time

import pytest
import yaml


def test_getcookies(driver):
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
    bef = driver.get_cookies()
    print("+++++++++" + str(bef))
    print(len(bef))
    time.sleep(10)
    cookies = driver.get_cookies()
    print("___________" + str(cookies))
    print(len(cookies))

    with open("/Users/potato/PycharmProjects/mywork/webwork/data/logincookies.yaml", "w") as f:
        yaml.dump(cookies, f)
