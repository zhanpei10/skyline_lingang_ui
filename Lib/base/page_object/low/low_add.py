'''
新建法律法规
'''
from Lib.base.keywords import KeyWords
from selenium.webdriver.common.by import By
from Lib.common.common_function import *
from Lib.base.page_object.login_page import LonginPage


class LowAdd(KeyWords):
    url = KeyWords.url + 'laws-center/create'
    # 新增法律法规的相关参数
    # 执法分类
    low_fl = (By.XPATH, '//label[text()="执法分类"]/../div[1]//input')
    # 法律法规库
    low_k = (By.XPATH, '//label[text()="法律法规库"]/../div[1]//input')
    # 违法名称
    illegal_name = (By.XPATH, '//label[text()="违法行为名称"]/../div[1]//input')
    # 法律法规规章规定
    low_gd = (By.XPATH, '//label[text()="法律法规规章规定"]/../div[1]//textarea')
    # 法律责任适用条款
    low_tk = (By.XPATH, '//label[text()="法律责任适用条款"]/../div[1]//textarea')
    # 选择浦东城管
    choose = (By.XPATH, '//label[text()="浦东城管"]/../div[1]//span[1]/span')
    # 点击新建
    create = (By.XPATH, '//span[text()="新建"]')

    def low_add(self):
        '''
        新建法律法规
        :return:
        '''
        self.open(self.url)
        self.wait(2)
        self.input_value(args=self.low_fl, text="自动化执法分类", context="执法分类")
        self.input_value(args=self.low_k, text="自动化法律法规库", context="法律法规库")
        self.input_value(args=self.illegal_name, text="自动化违法行为名称", context="违法行为名称")
        self.input_value(args=self.low_gd, text="自动化法律法规规章规定", context="法律法规规章规定")
        self.input_value(args=self.low_tk, text="自动化法律责任适用条款", context="法律责任适用条款")
        # 选择浦东城管
        self.click(args=self.choose, context="浦东城管")
        self.wait(1)
        self.click(args=self.create, context="新建")
        self.wait(2)


if __name__ == '__main__':
    driver = choose_browser()
    L = LonginPage(driver)
    L.login('kobeAdmin002', 'kobe8888')
    case = LowAdd(driver)
    case.low_add()
