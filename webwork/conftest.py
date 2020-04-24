import time

import pytest
import yaml
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome(
        executable_path='/usr/local/bin/chromdriver')
    driver.implicitly_wait(5)
    driver.maximize_window()
    return driver



