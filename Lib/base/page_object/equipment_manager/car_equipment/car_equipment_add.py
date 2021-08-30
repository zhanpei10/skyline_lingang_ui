'''
新增车载装备
'''
from Lib.base.keywords import KeyWords
from selenium.webdriver.common.by import By
from Lib.common.common_function import *
from Lib.base.page_object.login_page import LonginPage


class CarEquipment(KeyWords):
    url = KeyWords.url + 'equipmentManagement/VehicleEquipmentAdd'
    # 新增数据相关参数
    equipment_name = (By.XPATH, '//input[@placeholder="请输入设备名称"]')
    equipment_type = (By.XPATH, '//input[@placeholder="请选择设备类型"]')
    equipment_type_value = (By.XPATH, '//span[text()="车载视频终端"]')
    equipment_mark = (By.XPATH, '//input[@placeholder="请输入设备品牌"]')
    equipment_model = (By.XPATH, '//input[@placeholder="请输入设备型号"]')
    buy_time = (By.XPATH, '//input[@placeholder="请选择购置日期"]')
    buy_time_sure = (By.XPATH, '//label[text()="购置日期"]')
    # 选择车辆
    relevance_car = (By.XPATH, '//input[@placeholder="请选择车牌号码"]')
    relevance_car_value = (By.XPATH, '//span[text()="沪TEST01"]')
    # 点击确认
    add_sure = (By.XPATH, '//span[text()="确定"]')

    def car_equipment_add(self):
        '''
        新增车载装备
        :return:
        '''
        self.open(self.url)
        self.wait(3)
        self.input_value(args=self.equipment_name, text="自动化设备名称", context='设备名称')
        self.click(args=self.equipment_type, context="设备类型")
        self.wait(1)
        self.click(args=self.equipment_type_value, context="车载视频终端")
        self.input_value(args=self.equipment_mark, text="测试设备品牌", context='设备品牌')
        self.input_value(args=self.equipment_model, text="测试设备型号", context='设备型号')
        self.input_value(args=self.buy_time, text=get_time('%Y-%m-%d', -10), context='购置日期')
        self.click(args=self.buy_time_sure, context="购置日期")
        # 关联车辆
        self.click(args=self.relevance_car, context="关联车辆")
        self.wait(1)
        self.click(args=self.relevance_car_value, context="车辆")
        self.wait(1)
        self.click(args=self.add_sure, context="确定")


if __name__ == '__main__':
    driver = choose_browser()
    L = LonginPage(driver)
    L.login('kobeAdmin002', 'kobe8888')
    case = CarEquipment(driver)
    case.car_equipment_add()
