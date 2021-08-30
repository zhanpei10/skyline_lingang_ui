'''
其他装备列表查询和搜索 、编辑 和查看详情
'''

from Lib.base.keywords import KeyWords
from selenium.webdriver.common.by import By
from Lib.common.common_function import *
from Lib.base.page_object.login_page import LonginPage


class OtherEquipmentList(KeyWords):
    url = KeyWords.url + 'equipmentManagement/vehicleEquipment'
    # 进入其他装备页面
    other_equipment_view = (By.XPATH, '//div[contains(text(), "其他装备")]')
    # 设备类型
    other_equipment_type = (By.XPATH, '//div[@class="vehicle-list-filter"]//div[contains(text(), "设备类型")]//input')
    other_equipment_type_value1 = (By.XPATH, '//div[@x-placement = "bottom-start"]//span[text()="便携式打印机"]')
    other_equipment_type_value2 = (By.XPATH, '//div[@x-placement = "bottom-start"]//span[text()="不限"]')
    # 使用情况
    other_use_status = (By.XPATH, '//div[@class="vehicle-list-filter"]//div[contains(text(), "使用情况")]//input')
    other_use_status_value1 = (By.XPATH, '//div[@x-placement = "bottom-start"]//span[text()="正常"]')
    other_use_status_value2 = (By.XPATH, '//div[@x-placement = "bottom-start"]//span[text()="不限"]')

    # --------------------------搜索并查看详情-------------------------------------
    # 关键字搜索
    search_input = (By.XPATH, '//input[@placeholder="请输入设备名称"]')
    search_button = (By.XPATH, '//i[contains(@class, "rz-search-input-suffix" )]')
    search_clear = (By.XPATH, '//i[contains(@class, "rz-input__clear")]')
    # 查看详情
    detail_button = (By.XPATH, '//tr[@class = "rz-table__row"]//button/span[text()="详情"]')

    # -----------------------------编辑------------------------------------
    update_button = (By.XPATH, '//tr[@class = "rz-table__row"]//button/span[text()="编辑"]')
    # 编辑相关的详情
    other_equipment_name = (By.XPATH, '//input[@placeholder="请输入设备名称"]')
    other_equipment_mark = (By.XPATH, '//input[@placeholder="请输入设备品牌"]')
    # 确认修改
    update_sure = (By.XPATH, '//span[text()="确定"]')

    # ---------------------------删除操作-----------------------------------
    delete_button = (By.XPATH, '//tr[@class = "rz-table__row"]//button/span[text()="删除"]')
    delete_sure = (By.XPATH, '//span[contains(text(), "确定")]')

    def other_equipment_list(self):
        '''
        查询其他装备列表
        :return:
        '''
        self.open(self.url)
        self.wait(2)
        self.click(args=self.other_equipment_view, context="其他装备")
        self.wait(1)
        self.click(args=self.other_equipment_type, context="设备类型下拉框")
        self.wait(1)
        self.click(args=self.other_equipment_type_value1, context="便携式打印机")
        self.wait(1)
        self.click(args=self.other_equipment_type, context="设备类型下拉框")
        self.wait(1)
        self.click(args=self.other_equipment_type_value2, context="不限")
        # 点击使用情况
        self.click(args=self.other_use_status, context="使用情况")
        self.wait(1)
        self.click(args=self.other_use_status_value1, context="正常")
        self.wait(1)
        self.click(args=self.other_use_status, context="使用情况")
        self.wait(1)
        self.click(args=self.other_use_status_value2, context="不限")
        self.wait(1)

    def other_equipment_search_detail(self):
        '''
        搜索单兵装备和查看详情
        :return:
        '''
        self.open(self.url)
        self.wait(2)
        self.click(args=self.other_equipment_view, context="其他装备")
        # 模糊搜索
        self.wait(1)
        self.input_value(args=self.search_input, text='自动化', context="搜索输入框")
        self.click(args=self.search_button, context="搜索按钮")
        self.wait(1)
        # 清空输入框
        self.hover(args=self.search_input, context="搜索输入框")
        self.click(args=self.search_clear, context="清空按钮")
        # 精确搜索
        self.input_value(args=self.search_input, text="自动化设备名称", context="搜索输入框")
        self.click(args=self.search_button, context="搜索按钮")
        self.wait(1)
        # 查看详情
        self.click(args=self.detail_button, context="详情")
        self.wait(2)

    def other_equipment_search_update(self):
        '''
        查询和编辑其他装备
        :return:
        '''
        self.open(self.url)
        self.wait(2)
        self.click(args=self.other_equipment_view, context="其他装备")
        # 精确搜索
        self.input_value(args=self.search_input, text="自动化设备名称", context="搜索输入框")
        self.click(args=self.search_button, context="搜索按钮")
        self.wait(1)
        # 点击编辑进入编辑页面
        self.click(args=self.update_button, context="编辑")
        self.wait(1)
        # 编辑相关信息
        self.clear_input(args=self.other_equipment_name, context="设备名称")
        self.input_value(args=self.other_equipment_name, text="自动化设备名称1", context="设备名称")
        self.clear_input(args=self.other_equipment_mark, context="设备品牌")
        self.input_value(args=self.other_equipment_mark, text="这是修改后的设备品牌", context="设备名称")
        self.wait(1)
        self.click(args=self.update_sure, context="确认")

    def other_equipment_search_delete(self):
        '''
        查询和删除其他装备
        :return:
        '''
        self.open(self.url)
        self.wait(2)
        self.click(args=self.other_equipment_view, context="其他装备")
        # 精确搜索
        self.input_value(args=self.search_input, text="自动化设备名称", context="搜索输入框")
        self.click(args=self.search_button, context="搜索按钮")
        self.wait(1)
        # 点击删除按钮
        self.click(args=self.delete_button, context="删除")
        self.wait(1)
        self.click(args=self.delete_sure, context="确定")
        self.wait(1)


if __name__ == '__main__':
    driver = choose_browser()
    L = LonginPage(driver)
    L.login('kobeAdmin002', 'kobe8888')
    case = OtherEquipmentList(driver)
    case.other_equipment_search_delete()
