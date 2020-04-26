import csv
import os
from unittest.mock import ANY

import xlrd as xlrd
import xlwt as xlwt
import yaml
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from logger import *


class Commont():
    driver: WebDriver

    ##定位元素
    def find(self, by, value) -> WebElement:
        element = self.driver.find_element(by, value)
        print(element)
        return element

    ##定位元素
    def find_value(self, value) -> WebElement:
        element = self.driver.find_element(*value)
        print(element)
        return element

    ##等待元素可点击状态
    def wait_click(self, by, value) -> WebElement:
        element = WebDriverWait(self.driver, 10, 1, ignored_exceptions=(TimeoutException)) \
            .until(expected_conditions.element_to_be_clickable((by, value)))
        return element

    ## js点击元素
    def click_by_js(self, by, value):
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element(by, value))

    ##等待元素可见
    def wait_see(self, by, value) -> WebElement:
        element = WebDriverWait(self.driver, 10, 1, ignored_exceptions=(TimeoutException)).until(
            expected_conditions.visibility_of_element_located((by, value)))
        return element

    ##等待元素消失
    def wait_no(self, by, value) -> WebElement:
        element = WebDriverWait(self.driver, 10, 1, ignored_exceptions=(TimeoutException)).until(
            expected_conditions.invisibility_of_element_located((by, value)))
        return element

    ##向下滑动到元素位置
    def find_scro(self, by, value) -> WebElement:
        element = self.driver.find_element(by, value)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
        return element

    # 向上滑动滚动条，跳转到目标元素处
    def find_by_js(self, by, value) -> WebElement:
        element = self.driver.driver.find_element(by, value)
        self.driver.execute_script('arguments[0].scrollIntoView(false);', element)
        return element

    ##获取窗口手柄
    def get_handle(self):
        handle = self.driver.current_window_handle
        return handle

    ##切换窗口
    def switch_window(self, handle1):
        # 等待有两个窗口
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))
        # Loop through until we find a new window handle
        for window_handle in self.driver.window_handles:
            if window_handle != handle1:
                self.driver.switch_to.window(window_handle)

    ##判断弹窗
    def switch_alert(self):
        # Wait for the alert to be displayed
        self.wait.until(expected_conditions.alert_is_present())
        # Store the alert in a variable for reuse
        alert = self.driver.switch_to.alert
        # Store the alert text in a variable
        text = alert.text

        # Press the Cancel button

    ##页面加载策略    alert.dismiss()
    def jiazai(self):
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.page_load_strategy = 'normal'
        driver = webdriver.Chrome(options=options)
        # Navigate to url
        driver.get("http://www.google.com")
        driver.quit()

    ##切换frame  frameset不用切 ，iframe和frame需要切换(id,name,下标，元素定位)

    def switch_frame(self, search: ANY):
        self.driver.switch_to.frame(search)
        return self

    ##切换到 主页面主文档 frame
    def switch_defaule(self):
        self.driver.switch_to.default_content()
        return self

    # 切换到主frame
    def switch_parent_frame(self):
        self.driver.switch_to.parent_frame()
        return self

    ##获取当前文件的上级目录
    def file_path(self, file_name):

        dirpath = os.path.dirname(os.path.realpath(__file__))
        filepath = os.path.join(dirpath + '/../', file_name)
        logger.debug("文件的名字{}  文件的上级目录为{}  文件路径为{}".format(file_name, dirpath, filepath))

        return filepath

    ##读取yanml文件
    def read_yaml(self, filepath):
        with open(filepath, 'r') as f:
            data = yaml.load(f)
            logger.debug("yaml文件内容为{}".format(data))
        return data

    ##向yaml文件中写入
    def writ_yaml(self, filepath, data):
        with open(filepath, 'w') as f:
            yaml.dump(data, f)

    ##读取excel数据
    def read_excel(self, filepath, sheet_name):
        with xlrd.open_workbook(filepath) as f:
            # 1.获取sheet的名字
            # 1.1 获取所有sheet的名字(list类型)
            allSheetNames = f.sheet_names();
            print(allSheetNames);

            # 1.2 按索引号获取sheet的名字（string类型）
            sheet1Name = f.sheet_names()[0];
            print(sheet1Name);

            # 2. 获取sheet内容
            ## 2.1 法1：按索引号获取sheet内容
            # sheet1_content1 = f.sheet_by_index(0);  # sheet索引从0开始
            ## 2.2 法2：按sheet名字获取sheet内容
            sheet1_content1 = f.sheet_by_name(sheet_name);

            # 3. sheet的名称，行数，列数
            ##print(sheet1_content1.name, sheet1_content1.nrows, sheet1_content1.ncols);
            ##获取行数
            nrows = sheet1_content1.nrows
            ##获取列数
            ncols = sheet1_content1.ncols
            logger.debug("行数为{}  列数为{}".format(nrows, ncols))
            # 4. 获取整行和整列的值（数组）
            datat = ()
            for i in range(nrows):
                ##rowsdatta = sheet1_content1.row_values(i);  # 获取第一行内容

                for j in range(ncols):
                    ##colsdatat = sheet1_content1.col_values(j);  # 获取第三列内容
                    celldata = sheet1_content1.cell_value(i, j)  ##获取第几行第几咧的数据
                    data = (celldata)
                    logger.debug('哪行哪列数据::{}'.format(data))
            return data

            # # 5. 获取单元格内容(三种方式)
            # print(sheet1_content1.cell(1, 0).value);
            # print(sheet1_content1.cell_value(2, 2));
            # print(sheet1_content1.row(2)[2].value)
            #
            # # 6. 获取单元格内容的数据类型
            # # Tips: python读取excel中单元格的内容返回的有5种类型 [0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error]
            # t=sheet1_content1.cell(2, 0).ctype
            # logger.debug('数据的属性为{}'.format(t))

    def get_data_from_excel(excel_dir):  # 读取excel，取出所有sheet要执行的接口信息，返回列表
        work_book = xlrd.open_workbook(excel_dir)
        all_sheets = work_book.sheetnames
        api_info_list = []
        for i in range(0, len(all_sheets)):
            work_sheet = all_sheets[i]
            sheet = work_book[work_sheet]
            rows = sheet.max_row
            for r in range(1, rows):  # 从第2行开始取数据
                api_data = {}
                temp_list = []
                for n in range(0, len(sheet[str(r + 1)])):
                    if sheet[str(r + 1)][0].value == 1:  # 把标识为1的行，此行的每个单元格数据加入到临时list
                        temp_list.append(sheet[str(r + 1)][n].value)
                for param in temp_list:  # 把临时表list中有'='符号的元素分割开
                    if '=' in str(param):
                        p = param.split('=')
                        api_data[p[0]] = p[1]
                if api_data:
                    api_info_list.append(api_data)
        return api_info_list

    def read_txt(self, filepath):
        with open(filepath, 'r') as f:
            data = f.read()
        return data

    def read_csv(self, filepath):
        with open(filepath, 'r') as f:
            data = csv.reader(f)
        return data
