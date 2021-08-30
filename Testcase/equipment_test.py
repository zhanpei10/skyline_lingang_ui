'''
装备管理相关页面测试
'''
import unittest
from Lib.common.common_function import *
from Lib.base.page_object.login_page import LonginPage
from Lib.base.page_object.car_manager.car_add import CarAdd
from Lib.base.page_object.equipment_manager.car_equipment.car_equipment_add import CarEquipment
from Lib.base.page_object.equipment_manager.car_equipment.car_equipment_list import CarEquipmentList
from Lib.base.page_object.car_manager.car_list import CarList
from Lib.base.page_object.equipment_manager.single_equipment.single_equipment_add import SingleEquipmentAdd
from Lib.base.page_object.equipment_manager.single_equipment.single_equipment_list import SingleEquipmentList
from Lib.base.page_object.equipment_manager.other_equipment.other_equipment_add import OtherEquipmentAdd
from Lib.base.page_object.equipment_manager.other_equipment.other_equipment_list import OtherEquipmentList

from selenium.webdriver.common.by import By
from Lib.base.keywords import KeyWords
from Lib.common.ui_log import normal_log


class TestCar(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        normal_log().info('>>>>>装备管理相关页面测试开始')
        cls.driver = choose_browser()
        cls.kw = KeyWords(cls.driver)
        cls.login = LonginPage(cls.driver)
        cls.car = CarAdd(cls.driver)
        cls.equipmentAdd = CarEquipment(cls.driver)
        cls.equipmentList = CarEquipmentList(cls.driver)
        cls.carList = CarList(cls.driver)
        cls.singleEquipment = SingleEquipmentAdd(cls.driver)
        cls.singleEquipmentList = SingleEquipmentList(cls.driver)
        cls.otherEquipmentAdd = OtherEquipmentAdd(cls.driver)
        cls.otherEquipmentList = OtherEquipmentList(cls.driver)
        cls.login.login('kobeAdmin002', 'kobe8888')

    @classmethod
    def tearDownClass(cls) -> None:
        normal_log().info('>>>>>装备管理相关页面测试结束')
        cls.login.login_out()
        cls.driver.quit()

    def setUp(self) -> None:
        normal_log().info('>>>>>>>>>>>>>>>>>>>当前用例测试开始>>>>>>>>>>>>>>>>>>>>>>')

    def tearDown(self) -> None:
        # self.login.login_out()
        normal_log().info('>>>>>>>>>>>>>>>>>>>当前用例测试结束>>>>>>>>>>>>>>>>>>>>>>')

    def test_01_add_equipment(self):
        '''
        新增一个车载装备
        :return:
        '''
        normal_log().info('>>>>>新建车载装备开始')
        # 新增关联的车辆
        self.car.car_add()
        self.kw.wait(2)
        # 新增车载装备
        self.equipmentAdd.car_equipment_add()
        # 设置断言
        assert_args = (By.XPATH, '//p[contains(text(), "创建成功")]')
        self.kw.make_assert_by_text(args=assert_args, assert_data='创建成功', context='创建车载装备')

    def test_02_equipment_list(self):
        '''
        查询车载装备列表
        :return:
        '''
        normal_log().info('>>>>>>查看车载装备列表测试开始')
        self.equipmentList.car_equipment_list()
        # 设置断言
        assert_args = (By.XPATH, '//table[@class="rz-table__body"]//p[text()="自动化设备名称"]')
        self.kw.make_assert_by_text(args=assert_args, assert_data='自动化设备名称', context="查询车载装备列表")

    def test_03_equipment_search_detail(self):
        '''
        搜索车载装备并查看详情
        :return:
        '''
        normal_log().info('>>>>>>搜索车载装备和查看详情测试开始')
        self.equipmentList.car_equipment_search_detail()
        # 设置断言
        assert_args = (By.XPATH, '//span[text()="车载装备详情"]')
        self.kw.make_assert_by_text(args=assert_args, assert_data='车载装备详情', context="查看车载装备详情")

    def test_04_equipment_search_update(self):
        '''
        搜索车载装备并编辑
        :return:
        '''
        normal_log().info('>>>>>>搜索车载装备和编辑测试开始')
        self.equipmentList.car_equipment_search_update()
        # 设置断言
        assert_args = (By.XPATH, '//p[text()="更新成功!"]')
        self.kw.make_assert_by_text(args=assert_args, assert_data='更新成功!', context="查看车载装备详情")

    def test_05_equipment_search_delete(self):
        '''
        搜索车载装备并删除
            :return:
            '''
        normal_log().info('>>>>>>搜索车载装备和删除测试开始')
        self.equipmentList.car_equipment_search_delete()
        # 设置断言 获取删除弹窗
        assert_args = (By.XPATH, '//p[contains(text(), "删除失败,该车载设备已安装")]')
        text = self.kw.get_text(args=assert_args, context="删除弹窗")
        # 关联车辆无法删除
        if "删除失败,该车载设备已安装至车辆" in text:
            # 删除车辆 自动删除设备
            self.carList.car_detail_delete()
            assert_args = (By.XPATH, '//p[contains(text(), "暂无数据")]')
            self.kw.make_assert_by_text(args=assert_args, assert_data="暂无数据", context="删除车辆")
        else:
            self.kw.make_assert_by_text(args=assert_args, assert_data="暂无数据", context="删除车辆")

    def test_06_add_single_equipment(self):
        '''
        创建单兵装备
        :return:
        '''
        normal_log().info('>>>>>新建单兵装备开始')
        # 新增车载装备
        self.singleEquipment.single_equipment_add()
        # 设置断言
        assert_args = (By.XPATH, '//p[contains(text(), "创建成功")]')
        self.kw.make_assert_by_text(args=assert_args, assert_data='创建成功', context='创建单兵装备')

    def test_07_single_equipment_list(self):
        '''
        查看单兵装备列表
        :return:
        '''
        normal_log().info('>>>>>>搜索车载装备和查看详情测试开始')
        self.singleEquipmentList.single_equipment_list()
        # 设置断言
        assert_args = (By.XPATH, '//table[@class="rz-table__body"]//p[text()="自动化设备名称"]')
        self.kw.make_assert_by_text(args=assert_args, assert_data='自动化设备名称', context="单兵装备列表")

    def test_08_single_equipment_search_detail(self):
        '''
        查看单兵装备列表
        :return:
        '''
        normal_log().info('>>>>>>搜索车载装备和查看详情测试开始')
        self.singleEquipmentList.single_equipment_search_detail()
        # 设置断言
        assert_args = (By.XPATH, '//span[text()="单兵装备详情"]')
        self.kw.make_assert_by_text(args=assert_args, assert_data='单兵装备详情', context="单兵装备详情")

    def test_09_equipment_search_update(self):
        '''
        搜索车载装备并编辑
        :return:
        '''
        normal_log().info('>>>>>>搜索单兵装备和编辑测试开始')
        self.singleEquipmentList.single_equipment_search_update()
        # 设置断言
        assert_args = (By.XPATH, '//p[text()="更新成功!"]')
        self.kw.make_assert_by_text(args=assert_args, assert_data='更新成功!', context="修改单兵装备")

    def test_10_equipment_search_delete(self):
        '''
        搜索车载装备并编辑
        :return:
        '''
        normal_log().info('>>>>>>搜索单兵装备和删除测试开始')
        self.singleEquipmentList.single_equipment_search_delete()
        # 设置断言
        assert_args = (By.XPATH, '//p[text()="所选单兵装备已删除"]')
        self.kw.make_assert_by_text(args=assert_args, assert_data='所选单兵装备已删除', context="删除单兵装备")

    def test_11_add_other_equipment(self):
        '''
        创建单兵装备
        :return:
        '''
        normal_log().info('>>>>>新建其他装备开始')
        # 新增车载装备
        self.otherEquipmentAdd.other_equipment_add()
        # 设置断言
        assert_args = (By.XPATH, '//p[contains(text(), "创建成功")]')
        self.kw.make_assert_by_text(args=assert_args, assert_data='创建成功', context='创建其他装备')

    def test_12_other_equipment_list(self):
        '''
        查看单兵装备列表
        :return:
        '''
        normal_log().info('>>>>>>搜索其他装备和查看详情测试开始')
        self.otherEquipmentList.other_equipment_list()
        # 设置断言
        assert_args = (By.XPATH, '//table[@class="rz-table__body"]//p[text()="自动化设备名称"]')
        self.kw.make_assert_by_text(args=assert_args, assert_data='自动化设备名称', context="单兵装备列表")

    def test_13_other_equipment_search_detail(self):
        '''
        查看单兵装备列表
        :return:
        '''
        normal_log().info('>>>>>>搜索车载装备和查看详情测试开始')
        self.otherEquipmentList.other_equipment_search_detail()
        # 设置断言
        assert_args = (By.XPATH, '//span[text()="其他装备详情"]')
        self.kw.make_assert_by_text(args=assert_args, assert_data='其他装备详情', context="其他装备详情")

    def test_14_other_equipment_search_update(self):
        '''
        搜索车载装备并编辑
        :return:
        '''
        normal_log().info('>>>>>>搜索其他装备和编辑测试开始')
        self.otherEquipmentList.other_equipment_search_update()
        # 设置断言
        assert_args = (By.XPATH, '//p[text()="更新成功!"]')
        self.kw.make_assert_by_text(args=assert_args, assert_data='更新成功!', context="修改其他装备")

    def test_15_other_equipment_search_delete(self):
        '''
        搜索车载装备并编辑
        :return:
        '''
        normal_log().info('>>>>>>搜索其他装备和删除测试开始')
        self.otherEquipmentList.other_equipment_search_delete()
        # 设置断言
        assert_args = (By.XPATH, '//p[text()="所选其他装备已删除"]')
        self.kw.make_assert_by_text(args=assert_args, assert_data='所选其他装备已删除', context="删除其他装备")


if __name__ == '__main__':
    unittest.main()
