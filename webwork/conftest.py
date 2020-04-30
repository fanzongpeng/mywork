import time

import pytest
import yaml
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            # desired_capabilities=DesiredCapabilities.,
            desired_capabilities={'platform': 'ANY', 'browserName': 'chrome', 'version': '',
                                  'javascriptEnabled': True}
        )
    driver.implicitly_wait(5)
    driver.maximize_window()
    return driver



