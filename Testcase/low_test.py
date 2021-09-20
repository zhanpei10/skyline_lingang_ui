'''
会议管理UI测试
'''
import unittest
from Lib.common.common_function import *
from Lib.base.page_object.login_page import LonginPage
from Lib.base.page_object.low.low_add import LowAdd
from Lib.base.page_object.low.low_list import LowList
from selenium.webdriver.common.by import By
from Lib.base.keywords import KeyWords
from Lib.common.ui_log import normal_log


class MeetingTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        normal_log().info('>>>>>会议管理页面测试开始')
        cls.driver = choose_browser()
        cls.kw = KeyWords(cls.driver)
        cls.login = LonginPage(cls.driver)
        cls.lowAdd = LowAdd(cls.driver)
        cls.lowList = LowList(cls.driver)
        cls.login.login('kobeAdmin002', 'kobe8888')

    @classmethod
    def tearDownClass(cls) -> None:
        normal_log().info('>>>>>会议管理页面测试结束')
        cls.login.login_out()
        cls.driver.quit()

    def setUp(self) -> None:
        normal_log().info('>>>>>>>>>>>>>>>>>>>当前用例测试开始>>>>>>>>>>>>>>>>>>>>>>')

    def tearDown(self) -> None:
        # self.login.login_out()
        normal_log().info('>>>>>>>>>>>>>>>>>>>当前用例测试结束>>>>>>>>>>>>>>>>>>>>>>')

    def test_01_low_add(self):
        '''
        新建法律法规
        :return:
        '''
        normal_log().info('>>>>>新建法律法规开始')
        self.lowAdd.low_add()
        # 获取断言
        assert_args = (By.XPATH, '//p[contains(text(), "创建成功")]')
        self.kw.make_assert_by_text(args=assert_args, assert_data='创建成功', context="创建法律法规")

    def test_02_low_search_and_detail(self):
        '''
        新建法律法规
        :return:
        '''
        normal_log().info('>>>>>搜索和查看法律法规开始')
        self.lowList.low_search_and_detail()
        # 获取断言
        assert_args = (By.XPATH, '//span[text()="查看法律法规"]')
        self.kw.make_assert_by_text(args=assert_args, assert_data='查看法律法规', context="查看法律法规")

    def test_03_low_search_and_update(self):
        '''
        新建法律法规
        :return:
        '''
        normal_log().info('>>>>>搜索和查看法律法规开始')
        self.lowList.low_search_and_update()
        # 获取断言
        assert_args = (By.XPATH, '//p[contains(text(), "更新成功")]')
        self.kw.make_assert_by_text(args=assert_args, assert_data='更新成功', context="查看法律法规")

    def test_04_low_search_and_delete(self):
        '''
        新建法律法规
        :return:
        '''
        normal_log().info('>>>>>搜索和查看法律法规开始')
        self.lowList.low_search_and_delete()
        # 获取断言
        assert_args = (By.XPATH, '//p[contains(text(), "删除成功")]')
        self.kw.make_assert_by_text(args=assert_args, assert_data='删除成功', context="查看法律法规")


if __name__ == '__main__':
    unittest.main()
