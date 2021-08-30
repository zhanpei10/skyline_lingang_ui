'''
会议管理UI测试
'''
import unittest
from Lib.common.common_function import *
from Lib.base.page_object.login_page import LonginPage
from Lib.base.page_object.meeting_manager.meeting_add import MeetingAdd
from Lib.base.page_object.meeting_manager.meeting_list import MeetingList
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
        cls.meetingAdd = MeetingAdd(cls.driver)
        cls.meetingList = MeetingList(cls.driver)
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

    def test_01_meeting_add(self):
        '''
        新增会议草稿和会议详情
        :return:
        '''
        normal_log().info('>>>>新增会议管理测试开始')
        self.meetingAdd.add_meeting()
        assert_data = (By.XPATH, '//p[text()="编辑成功"]')
        self.kw.make_assert_by_text(args=assert_data, assert_data='编辑成功', context='新增会议')

    def test_02_meeting_list(self):
        '''
        对会议列表进行筛选
        :return:
        '''
        normal_log().info('>>>>查看会议列表测试开始')
        self.meetingList.list_screen()
        assert_data = (By.XPATH, '//table[@class="rz-table__body"]/tbody/tr[1]/td[1]')
        self.kw.make_assert_by_text(args=assert_data, assert_data='这是自动化的会议主题', context='查询列表')

    def test_03_meeting_detail_update(self):
        '''
        查看会议详情和修改会议
        :return:
        '''
        normal_log().info('>>>>查看会议详情和修改会议测试开始')
        self.meetingList.look_detail_update()
        assert_data = (By.XPATH, '//p[text()="编辑成功"]')
        self.kw.make_assert_by_text(args=assert_data, assert_data='编辑成功', context='编辑和查看详情')

    def test_04_meeting_cancel(self):
        '''
        取消会议通知
        :return:
        '''
        normal_log().info('>>>>>取消会议通知测试开始')
        self.meetingList.cancel_meeting()
        assert_args = (By.XPATH, '//p[contains(text(), "取消成功")]')
        self.kw.make_assert_by_text(args=assert_args, assert_data='取消成功！', context='取消会议通知')


if __name__ == '__main__':
    unittest.main()
