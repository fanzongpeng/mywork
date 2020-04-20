import pytest

from webwork.page.bashpage import BashPage


class TestBash():

    def test_main(self,driver):
        BashPage(driver)