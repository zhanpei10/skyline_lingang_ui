'''
专项整治功能测试
'''
import unittest
from ddt import ddt, data, unpack
from Lib.common.common_function import *
from Lib.base.page_object.login_page import LonginPage
from Lib.base.page_object.special_rectification_list import SpecialRectificationList
from Lib.base.page_object.special_rectification_add import SpecialRectificationAdd
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
        cls.special_rectification_list = SpecialRectificationList(cls.driver)
        cls.special_rectification_add = SpecialRectificationAdd(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        normal_log().info('>>>>>事件管理页面测试结束')
        cls.driver.quit()

    def setUp(self) -> None:
        self.login.login('kobeAdmin002', 'kobe8888')

    def tearDown(self) -> None:
        self.login.login_out()

    def test_1_special_rectification_add_to_draft(self):
        '''
        新增专项整治
        :return:
        '''
        normal_log().info('>>>>新增专项整治草稿箱开始')
        self.special_rectification_add.add_special_rectification()
        # 设置断言
        assert_arg = (By.XPATH, '//p[text()="编辑成功"]')
        self.kw.make_assert_by_text(args=assert_arg, assert_data='编辑成功', context='编辑成功弹窗')

    def test_2_special_rectification_filter(self):
        '''
        筛选相关功能测试
        :return:
        '''
        normal_log().info('>>>>专项整治筛选相关功能测试开始')
        self.special_rectification_list.special_rectification_filter()
        # 设置断言
        assert_args = (By.XPATH, '//div[@class="list-view-content"]/div[1]/div[1]/div[2]/p')
        self.kw.make_assert_by_text(args=assert_args, assert_data='专项整治', context='标题')

    def test_3_special_rectification_detail_and_update(self):
        '''
        查看专项整治详情，并进行编辑
        :return:
        '''
        normal_log().info('>>>>查看和编辑专项整治详情开始')
        self.special_rectification_list.special_rectification_detail_and_update()
        # 设置断言
        assert_args = (By.XPATH, '//div[@role="alert"]/p')
        self.special_rectification_list.make_assert_by_text(args=assert_args, assert_data='编辑成功', context='编辑成功弹窗')

    def test_4_special_rectification_add_work_log(self):
        '''
        添加工作日志
        :return:
        '''
        normal_log().info('>>>>添加工作日志开始')
        self.special_rectification_list.special_rectification_add_work_log()
        # 设置断言
        assert_args = (By.XPATH, '//div[text() = "暂无数据"]')
        self.kw.make_assert_by_text(args=assert_args, assert_data='暂无数据', context='日志内容元素')

    def test_5_special_rectification_detail_flow(self):
        '''
        专项整治流转流程
        :return:
        '''
        normal_log().info('>>>>>专项整治流转开始')
        self.special_rectification_list.special_rectification_detail_flow()
        # 设置断言
        assert_args = (By.XPATH, '//p[text()="流转成功"]')
        self.kw.make_assert_by_text(args=assert_args, assert_data='流转成功', context='流转完成')


if __name__ == '__main__':
    unittest.main()
