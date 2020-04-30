from selenium.webdriver.common.by import By



class Testappium():

    def test_login(self,driver):


        driver.find_element(By.XPATH,"//*[@text='我的']").click()
        driver.find_element(By.XPATH,"//*[@text='手机号']").click()
        driver.find_element(By.XPATH,"//*[@text='邮箱手机号密码登录']").click()





