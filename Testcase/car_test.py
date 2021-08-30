'''
车辆管理相关页面测试
'''
import unittest
from Lib.common.common_function import *
from Lib.base.page_object.login_page import LonginPage
from Lib.base.page_object.car_manager.car_add import CarAdd
from Lib.base.page_object.car_manager.car_list import CarList
from selenium.webdriver.common.by import By
from Lib.base.keywords import KeyWords
from Lib.common.ui_log import normal_log


class TestCar(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        normal_log().info('>>>>>车辆管理相关页面测试开始')
        cls.driver = choose_browser()
        cls.kw = KeyWords(cls.driver)
        cls.login = LonginPage(cls.driver)
        cls.car = CarAdd(cls.driver)
        cls.car_list = CarList(cls.driver)
        cls.login.login('kobeAdmin002', 'kobe8888')

    @classmethod
    def tearDownClass(cls) -> None:
        normal_log().info('>>>>>车辆管理相关页面测试结束')
        cls.login.login_out()
        cls.driver.quit()

    def setUp(self) -> None:
        normal_log().info('>>>>>>>>>>>>>>>>>>>>>>>>>当前用例测试开始>>>>>>>>>>>>>>>>>>>>')

    def tearDown(self) -> None:
        normal_log().info('>>>>>>>>>>>>>>>>>>>>>>>>>当前用例测试结束>>>>>>>>>>>>>>>>>>>>')

    def test_01_create_car(self):
        '''
        新建一个车辆
        :return:
        '''
        normal_log().info(">>>>新增车辆测试开始")
        self.car.car_add()
        # 设置断言
        assert_args = (By.XPATH, '//p[text()="创建成功！"]')
        self.kw.make_assert_by_text(args=assert_args, assert_data='创建成功', context='创建车辆')

    def test_02_car_list(self):
        '''
        查询车辆
        :return:
        '''
        normal_log().info('>>>>>查询车辆列表')
        self.car_list.car_list()
        # 设置断言
        assert_args = (By.XPATH, '//table[@class="rz-table__body"]//tr[1]/td[1]/div')
        self.kw.make_assert_by_text(args=assert_args, assert_data='沪TEST01', context="查询车辆列表")

    def test_03_car_search_detail(self):
        '''
        搜索车辆并查看详情
        :return:
        '''
        normal_log().info('>>>>搜索车辆并查看车辆详情')
        self.car_list.car_search_detail()
        # 设置断言
        assert_args = (By.XPATH, '//span[text()="查看车辆详情"]')
        self.kw.make_assert_by_text(args=assert_args, assert_data="查看车辆详情", context="查询车辆详情")

    def test_04_car_search_update(self):
        '''
        搜索车辆并查看详情
        :return:
        '''
        normal_log().info('>>>>搜索车辆之后并修改')
        self.car_list.car_search_update()
        # 设置断言
        assert_args = (By.XPATH, '//p[contains(text(), "更新成功")]')
        self.kw.make_assert_by_text(args=assert_args, assert_data="更新成功", context="修改车辆")

    def test_05_car_search_delete(self):
        '''
        搜索车辆并查看详情
        :return:
        '''
        normal_log().info('>>>>搜索车辆之后并修改')
        self.car_list.car_detail_delete()
        # 设置断言
        assert_args = (By.XPATH, '//p[contains(text(), "暂无数据")]')
        self.kw.make_assert_by_text(args=assert_args, assert_data="暂无数据", context="删除车辆")


if __name__ == '__main__':
    unittest.main()
