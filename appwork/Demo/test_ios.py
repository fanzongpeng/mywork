from time import sleep

from appium import webdriver


class TestIOS:

    def setup(self):
        caps = {}
        caps["platformName"] = "ios"
        caps["app"] = "/Users/potato/Library/Developer/Xcode/DerivedData/UICatalog-egvdhizdqtseyfacaesstqxmgusw/Build/Products/Debug-iphonesimulator/UICatalog.app"
        caps["automationName"] = "xcuitest"
        caps["deviceName"] = "iphone 11 pro"
        caps["platformVersion"] = "13.2"

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    def test_buttons(self):
        sleep(10)
        el1 = self.driver.find_element_by_accessibility_id("Buttons")
        el1.click()
        print("hahaha")

    def teardown(self):
        sleep(20)
        self.driver.quit()
