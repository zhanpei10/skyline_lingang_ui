'''
专项整治功能测试
'''
import unittest
from ddt import ddt, data, unpack
from Lib.common.common_function import *
from Lib.base.page_object.login_page import LonginPage
from Lib.base.page_object.special_rectification_list import SpecialRectification
from selenium.webdriver.common.by import By
from Lib.base.keywords import KeyWords
import pytest
from Lib.common.ui_log import error_log, normal_log


class SpecialRectificationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        normal_log().info('>>>>>专项整治页面测试开始')
        cls.driver = choose_browser()
        cls.kw = KeyWords(cls.driver)
        cls.login = LonginPage(cls.driver)
        cls.special_rectification = SpecialRectification(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        normal_log().info('>>>>>事件管理页面测试结束')
        cls.driver.quit()

    def setUp(self) -> None:
        self.login.login('kobeAdmin002', 'kobe8888')

    def tearDown(self) -> None:
        self.login.login_out()

    def test_special_rectification_filter(self):
        '''
        筛选相关功能测试
        :return:
        '''
        normal_log().info('>>>>专项整治筛选相关功能测试开始')
        self.special_rectification.special_rectification_filter()
        # 设置断言
        assert_args = (By.XPATH, '//div[@class="list-view-content"]/div[1]/div[1]/div[2]/p')
        self.kw.make_assert_by_text(args=assert_args, assert_data='测试', context='标题')

    def test_special_rectification_detail(self):
        '''
        查看专项整治详情，并进行编辑
        :return:
        '''
        normal_log().info('>>>>查看和编辑专项整治详情开始')
        self.special_rectification.special_rectification_detail()
        # 设置断言
        assert_args = (By.XPATH, '//div[@role="alert"]/p')
        self.special_rectification.make_assert_by_text(args=assert_args, assert_data='编辑成功', context='编辑成功弹窗')


if __name__ == '__main__':
    unittest.main()
