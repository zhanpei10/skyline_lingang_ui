# 事件管理页面测试
import unittest
from ddt import ddt, data, unpack
from Lib.common.common_function import *
from Lib.base.page_object.login_page import LonginPage
from Lib.base.page_object.case_manager import CaseManager
from selenium.webdriver.common.by import By
from Lib.base.keywords import KeyWords
import pytest
from Lib.common.ui_log import error_log, normal_log


@ddt
class CaseManagerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        normal_log().info('>>>>>事件管理页面测试开始')
        cls.driver = choose_browser()
        cls.kw = KeyWords(cls.driver)
        cls.login = LonginPage(cls.driver)
        cls.caseManager = CaseManager(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        normal_log().info('>>>>>事件管理页面测试结束')
        cls.driver.quit()

    def setUp(self) -> None:
        self.login.login('kobeAdmin002', 'kobe8888')

    def tearDown(self) -> None:
        self.login.login_out()

    def test_look_by_case_from(self):
        normal_log().info('>>>>>事件来源筛选测试：')
        self.caseManager.look_by_case_from()
        try:
            assert_args = (By.XPATH, '//table[@class="rz-table__body"]//tr[1]/td[10]/div/div')
            text = self.kw.get_text(args=assert_args, context='事件来源')
            self.assertEqual(text.strip(), 'AIOT感知', msg='事件来源错误')
        except AssertionError as e:
            self.kw.get_error_picture(context='事件来源应为AIOT感知')
            error_log().debug('>>>>>>事件来源筛选测试失败')
            error_log().debug('>>>>>>>{}'.format(e))
            raise e

    def test_look_by_case_type(self):
        normal_log().info('>>>>根据事件类型筛选事件')
        self.caseManager.look_by_case_type()
        try:
            assert_args = (By.XPATH, '//table[@class="rz-table__body"]//tr[1]/td[2]/div/div')
            text = self.kw.get_text(args=assert_args, context='执法分类')
            self.assertEqual(text.strip(), '规划', msg='事件类型错误')
        except AssertionError as e:
            self.kw.get_error_picture(context='执法分类应为规划')
            error_log().debug('>>>>筛选事件类型失败')
            error_log().debug('>>>>>>>>>>>>>>>{}'.format(e))
            raise e

    def test_look_by_case_stage(self):
        normal_log().info('>>>>>根据事件阶段筛选事件')
        self.caseManager.look_by_case_stage()
        try:
            assert_args = (By.XPATH, '//table[@class="rz-table__body"]//tr[1]/td[8]/div/div')
            text = self.kw.get_text(args=assert_args, context='事件阶段')
            self.assertEqual(text.strip(), '受理', msg='事件阶段筛选失败')
        except AssertionError as e:
            self.kw.get_error_picture(context='事件阶段应该为受理')
            error_log().debug('>>>>按事件阶段筛选失败')
            error_log().debug('>>>>>>>>>>>>>>>>>>>{}'.format(e))
            raise e

    def test_look_by_case_status(self):
        normal_log().info('>>>>>>>>>>>>>>事件状态测试开始')
        self.caseManager.look_by_case_status()
        # 设置断言
        assert_args = (By.XPATH, '//table[@class="rz-table__body"]//tr[1]/td[9]/div/span')
        self.kw.make_assert_by_text(args=assert_args, assert_data='已上报', context='事件状态')

    def test_look_by_case_time_and_keyword(self):
        normal_log().info('>>>>>>>>>>>>根据时间和关键字进行筛选')
        self.caseManager.look_by_case_time_and_keyword()
        # 设置断言
        assert_args = (By.XPATH, '//table[@class="rz-table__body"]//tr[1]/td[5]/div/span')
        self.kw.make_assert_by_text(args=assert_args, assert_data='上海', context='事发地点')

    def test_look_by_case_urgency_sort(self):
        '''
        事件排序操作
        :return:
        '''
        normal_log().info('>>>>>>>>>>>>>>>排序操作')
        self.caseManager.look_by_case_urgency_sort()
        # 设置断言
        assert_args1 = (By.XPATH, '//table[@class="rz-table__body"]//tr[1]/td[7]/div/div')
        assert_args2 = (By.XPATH, '//table[@class="rz-table__body"]//tr[2]/td[7]/div/div')
        self.kw.make_assert_by_compare_time(args1=assert_args1, args2=assert_args2, context="更新时间")

    def test_look_case_detail(self):
        '''
        查看事件详情
        :return:
        '''
        normal_log().info('>>>>>>>>>>>>>>>>>查看事件详情')
        self.caseManager.look_case_detail()
        # 设置断言
        assert_args = (By.XPATH, '//span[text()="违法信息"]')
        self.kw.make_assert_by_text(args=assert_args, assert_data='违法信息', context='违法信息')

    def test_look_case_already(self):
        '''
        查看已处理、 已过期、 未配置流程事件
        :return:
        '''
        normal_log().info('>>>>>>>查看已处理、 已过期、 未配置流程事件')
        self.caseManager.look_case_already()
        # 设置断言
        assert_args = (By.XPATH, '//span[text()="未配置流程的事件"]')
        self.kw.make_assert_by_text(args=assert_args, assert_data="未配置流程的事件")


if __name__ == '__main__':
    unittest.main()
