import pytest


@pytest.fixture(scope='session',autouse=True)
def login():
    print("\n输入用户名密码登陆！C")

