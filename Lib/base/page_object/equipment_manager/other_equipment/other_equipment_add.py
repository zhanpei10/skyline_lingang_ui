'''
单兵装备查询、编辑、删除相关操作
'''
from Lib.base.keywords import KeyWords
from selenium.webdriver.common.by import By
from Lib.common.common_function import *
from Lib.base.page_object.login_page import LonginPage


class OtherEquipmentAdd(KeyWords):
    url = KeyWords.url + 'equipmentManagement/ortherEquipmentAdd'

    # 新增数据相关参数
    other_equipment_name = (By.XPATH, '//input[@placeholder="请输入设备名称"]')
    other_equipment_type = (By.XPATH, '//input[@placeholder="请选择设备类型"]')
    other_equipment_type_value = (By.XPATH, '//span[text()="便携式打印机"]')
    other_equipment_mark = (By.XPATH, '//input[@placeholder="请输入设备品牌"]')
    other_equipment_model = (By.XPATH, '//input[@placeholder="请输入设备型号"]')
    other_buy_time = (By.XPATH, '//input[@placeholder="请选择购置日期"]')
    other_buy_time_sure = (By.XPATH, '//label[text()="购置日期"]')
    # 点击确认
    add_sure = (By.XPATH, '//span[text()="确定"]')

    def other_equipment_add(self):
        '''
        新增单兵装备
        :return:
        '''
        self.open(self.url)
        self.wait(2)
        # 填写新增相关参数
        self.input_value(args=self.other_equipment_name, text="自动化设备名称", context='设备名称')
        self.click(args=self.other_equipment_type, context="设备类型")
        self.wait(1)
        self.click(args=self.other_equipment_type_value, context="便携式打印机")
        self.input_value(args=self.other_equipment_mark, text="测试设备品牌", context='设备品牌')
        self.input_value(args=self.other_equipment_model, text="测试设备型号", context='设备型号')
        self.input_value(args=self.other_buy_time, text=get_time('%Y-%m-%d', -10), context='购置日期')
        self.click(args=self.other_buy_time_sure, context="购置日期")
        # 点击确定
        self.click(args=self.add_sure, context="确定")
        self.wait(2)


if __name__ == '__main__':
    driver = choose_browser()
    L = LonginPage(driver)
    L.login('kobeAdmin002', 'kobe8888')
    case = OtherEquipmentAdd(driver)
    case.other_equipment_add()
