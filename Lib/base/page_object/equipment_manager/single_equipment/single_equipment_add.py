from Lib.base.keywords import KeyWords
from selenium.webdriver.common.by import By
from Lib.common.common_function import *
from Lib.base.page_object.login_page import LonginPage

'''
新增单兵装备管理
'''


class SingleEquipmentAdd(KeyWords):
    url = KeyWords.url + 'equipmentManagement/singleEquipmentAdd'

    # 新增单兵装备相关元素
    single_equipment_view = (By.XPATH, '//div[contains(text(), "单兵装备")]')
    # 新增数据相关参数
    equipment_name = (By.XPATH, '//input[@placeholder="请输入设备名称"]')
    equipment_type = (By.XPATH, '//input[@placeholder="请选择设备类型"]')
    equipment_type_value = (By.XPATH, '//span[text()="执法记录仪"]')
    equipment_mark = (By.XPATH, '//input[@placeholder="请输入设备品牌"]')
    equipment_model = (By.XPATH, '//input[@placeholder="请输入设备型号"]')
    buy_time = (By.XPATH, '//input[@placeholder="请选择购置日期"]')
    buy_time_sure = (By.XPATH, '//label[text()="购置日期"]')
    # 关联用户
    use_people_name = (By.XPATH, '//input[@placeholder="请输人人员姓名"]')
    # 选择查询出来的人员
    use_people_name_value = (By.XPATH, '//span[text()="申请人kb"]')
    # 点击确认
    add_sure = (By.XPATH, '//span[text()="确定"]')

    def single_equipment_add(self):
        '''
        新增单兵装备
        :return:
        '''
        self.open(self.url)
        self.wait(2)
        # 填写新增相关参数
        self.input_value(args=self.equipment_name, text="自动化设备名称", context='设备名称')
        self.click(args=self.equipment_type, context="设备类型")
        self.wait(1)
        self.click(args=self.equipment_type_value, context="执法记录仪")
        self.input_value(args=self.equipment_mark, text="测试设备品牌", context='设备品牌')
        self.input_value(args=self.equipment_model, text="测试设备型号", context='设备型号')
        self.input_value(args=self.buy_time, text=get_time('%Y-%m-%d', -10), context='购置日期')
        self.click(args=self.buy_time_sure, context="购置日期")
        # 输入人员姓名
        self.input_value(args=self.use_people_name, text="申请人kb", context="使用人员")
        self.wait(2)
        self.click(args=self.use_people_name_value, context="申请人kb")
        # 点击确定
        self.click(args=self.add_sure, context="确定")
        self.wait(2)


if __name__ == '__main__':
    driver = choose_browser()
    L = LonginPage(driver)
    L.login('kobeAdmin002', 'kobe8888')
    case = SingleEquipmentAdd(driver)
    case.single_equipment_add()
