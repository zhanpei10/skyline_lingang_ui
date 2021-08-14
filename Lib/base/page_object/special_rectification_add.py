'''
新增专项整治
'''
from Lib.base.keywords import KeyWords
from selenium.webdriver.common.by import By
from Lib.common.common_function import *
from Lib.base.page_object.login_page import LonginPage


class SpecialRectification(KeyWords):
    '''
    专项整治类
    '''
    url = KeyWords.url + 'special-rectification/list'

    # 新增专项整治
    # 基础信息


    def special_rectification_filter(self):
        '''
        专项整治筛选相关的功能测试
        :return:
        '''
        self.open(self.url)


if __name__ == '__main__':
    driver = choose_browser()
    L = LonginPage(driver)
    L.login('kobeAdmin002', 'kobe8888')
    case = SpecialRectification(driver)
    case.special_rectification_detail()
