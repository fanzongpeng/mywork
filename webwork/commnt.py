import yaml
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions, wait

##
from selenium.webdriver.support.wait import WebDriverWait
driver:WebDriver
##定位元素
def find(driver, by, value) -> WebElement:
    element: WebElement
    # 加上重试机制
    ## for i in range(3):
    ##try:
    print(type(by),type(value))
    print(by,value)
    element = driver.find_element(by, value)
    return element
    # except:
    #     # 找到页面的最顶层元素进行点击
    #     # 动态变化位置的元素
    #
    #     # 黑名单
    #     ##//*[@text='弹框']/..//*[@text='确认']
    #     for e in BasePage.element_black:
    #         elements = self.driver.find_elements(*e)
    #         if (elements.__sizeof__() > 0):
    #             elements[0].click()


def find_ele(driver, kv) -> WebElement:
    element = driver.find_element(*kv)
    return element


##显示等待元素出现并可点击状态
def wait_click(driver, by, value) -> WebElement:
    element = WebDriverWait(driver, 10, 1, ignored_exceptions=(TimeoutException)).until(expected_conditions.element_to_be_clickable((by, value)))
    return element


##等待元素可见
def wait_see(driver, by,value) -> WebElement:
    element = WebDriverWait(driver, 10, 1, ignored_exceptions=(TimeoutException)).until(expected_conditions.visibility_of_element_located((by,value)))
    return element


##等待元素不可见，消失
def notsee(driver, by,value) -> WebElement:
    element = WebDriverWait(driver, 10, 1, ignored_exceptions=(TimeoutException)).until(expected_conditions.invisibility_of_element_located((by,value)))
    return element


##通过文本定位元素 xpath
def findByText(driver, text) -> WebElement:
    return find(driver, By.XPATH, "//*[@text='%s']" % text)


##js直接点击定位元素
def click_by_js(driver, by, value):
    driver.execute_script("arguments[0].click();",
        driver.find_element(by, value))
##向下滑动定位元素
def find_by_js(driver,by,value):
    element=driver.driver.find_element(by, value)
    driver.execute_script('arguments[0].scrollIntoView();', element)
    return element
# 向上滑动滚动条，跳转到目标元素处
def find_by_js(driver, by, value):
    element = driver.driver.find_element(by, value)
    driver.execute_script('arguments[0].scrollIntoView(false);', element)
    return element
    # arguments[
    #     0].scrollIntoView()，不能随意使用, 会先把元素element对象的表格“顶端”移动到与当前窗口的“顶部”对齐，如果元素当前可见，可能移动后就不可见了，导致定位报错。因为会把元素顶端对齐窗口顶部，有时候也会出现跳转后，元素仍然不可见的情况。
    #
    # 如果是需要点击这个元素，可以直接使用js驱动的方式（直接点击不可见的目标元素，不再先跳转），如下：
    # self.driver.execute_script(“arguments[0].click();”, el)
    # ————————————————
    # 版权声明：本文为CSDN博主「Kosmoo」的原创文章，遵循
    # CC
    # 4.0
    # BY - SA
    # 版权协议，转载请附上原文出处链接及本声明。
    # 原文链接：https: // blog.csdn.net / zwq912318834 / java / article / details / 79262007
##键盘enter
def enter():
    from selenium.webdriver.common.keys import Keys
    Keys.ENTER
##切换窗口
def switch_handel():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    # Start the driver
    with webdriver.Firefox() as driver:
        # Open URL
        driver.get("https://seleniumhq.github.io")

        # Setup wait for later
        wait = WebDriverWait(driver, 10)

        # Store the ID of the original window
        original_window = driver.current_window_handle

        # Check we don't have other windows open already
        assert len(driver.window_handles) == 1

        # Click the link which opens in a new window
        driver.find_element_by_link_text("new window").click()

        # Wait for the new window or tab
        wait.until(EC.number_of_windows_to_be(2))

        # Loop through until we find a new window handle
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        # Wait for the new tab to finish loading content
        wait.until(EC.title_is("SeleniumHQ Browser Automation"))
##判断弹窗
def al():
    driver.find_element_by_link_text("See a sample confirm").click()

    # Wait for the alert to be displayed
    wait.until(expected_conditions.alert_is_present())

    # Store the alert in a variable for reuse
    alert = driver.switch_to.alert

    # Store the alert text in a variable
    text = alert.text

    # Press the Cancel button
##页面加载策略    alert.dismiss()
def jiazai():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(options=options)
    # Navigate to url
    driver.get("http://www.google.com")
    driver.quit()
def file_path():
    pass


def read_yaml(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = yaml.load(f)
        print(data)
    return data
