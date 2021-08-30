'''
车辆管理的查询 编辑 和删除
'''

from Lib.base.keywords import KeyWords
from selenium.webdriver.common.by import By
from Lib.common.common_function import *
from Lib.base.page_object.login_page import LonginPage


class CarList(KeyWords):
    url = KeyWords.url + 'vehicle-center/query'
    # >>> 查询条件相关》》》
    # 车辆类型
    car_type = (By.XPATH, '//form/div[1]/div//input')
    car_type_value1 = (By.XPATH, '//div[@x-placement="bottom-start"]//span[text()="皮卡"]')
    car_type_value2 = (By.XPATH, '//div[@x-placement="bottom-start"]//span[text()="不限"]')
    # 车辆标识
    car_mark = (By.XPATH, '//form/div[2]/div//input')
    car_mark_value1 = (By.XPATH, '//div[@x-placement="bottom-start"]//span[text()="未涂装"]')
    car_mark_value2 = (By.XPATH, '//div[@x-placement="bottom-start"]//span[text()="不限"]')
    # 使用情况
    car_use = (By.XPATH, '//form/div[3]/div//input')
    car_use_value1 = (By.XPATH, '//div[@x-placement="bottom-start"]//span[text()="正常"]')
    car_use_value2 = (By.XPATH, '//div[@x-placement="bottom-start"]//span[text()="不限"]')
    # 使用部门
    use_org = (By.XPATH, '//form/div[4]/div//input')
    use_org_value1 = (By.XPATH, '//div[@x-placement="bottom-start"]/div[1]/div/ul/li[2]/span')
    use_org_value2 = (By.XPATH, '//div[@x-placement="bottom-start"]//span[text()="不限"]')

    # -------------------------------根据关键字进行搜索 查看详情 编辑和 删除---------------------------------------
    # 搜索操作
    search_element = (By.XPATH, '//input[contains(@placeholder, "请输入车牌")]')
    search_button = (By.XPATH, '//i[contains(@class, "rz-icon-search")]')
    # 清空搜索信息
    search_value_clear = (By.XPATH, '//i[contains(@class, "rz-input__clear")]')
    # 点击详情
    car_detail = (By.XPATH, '//div[contains(@class , "is-scrolling-none")]//span[text()="详情"]')
    # 查看车辆照片
    car_photo = (By.XPATH, '//span[text()="车辆照片"]')

    # 点击编辑
    car_update = (By.XPATH, '//div[contains(@class , "is-scrolling-none")]//span[text()="编辑"]')
    # 编辑车辆品牌
    car_brand = (By.XPATH, '//input[@placeholder = "请输入车辆品牌"]')
    # 点击确认
    car_update_sure = (By.XPATH, '//span[text()="确定"]')

    # 点击删除
    car_delete = (By.XPATH, '//div[contains(@class , "is-scrolling-none")]//span[text()="删除"]')
    # 点击确认
    car_delete_sure = (By.XPATH, '//span[contains(text(), "确定")]')

    def car_list(self):
        '''
        车辆列表查询和车辆详情查看
        :return:
        '''
        self.open(self.url)
        self.wait(3)
        # 车辆类型进行筛选
        self.click(args=self.car_type, context="车辆类型下拉框")
        self.wait(1)
        self.click(args=self.car_type_value1, context="皮卡")
        self.wait(1)
        self.click(args=self.car_type, context="车辆类型下拉框")
        self.wait(1)
        self.click(args=self.car_type_value2, context="不限")
        # 车辆标识
        self.click(args=self.car_mark, context="车辆标识下拉框")
        self.wait(1)
        self.click(args=self.car_mark_value1, context="未涂装")
        self.wait(1)
        self.click(args=self.car_mark, context="车辆标识下拉框")
        self.wait(1)
        self.click(args=self.car_mark_value2, context="不限")
        # 使用情况
        self.click(args=self.car_use, context="使用情况下拉框")
        self.wait(1)
        self.click(args=self.car_use_value1, context="正常")
        self.wait(1)
        self.click(args=self.car_use, context='使用情况下拉框')
        self.wait(1)
        self.click(args=self.car_use_value2, context="不限")
        # 使用部门
        self.click(args=self.use_org, context="使用部门下拉框")
        self.wait(1)
        self.click(args=self.use_org_value1, context="第一个部门")
        self.wait(1)
        self.click(args=self.use_org, context="使用部门下拉框")
        self.wait(1)
        self.click(args=self.use_org_value2, context="不限")
        self.wait(2)

    def car_search_detail(self):
        '''
        根据关键字进行搜索 查看详情 编辑和 删除
        :return:
        '''
        self.open(self.url)
        self.wait(3)
        # 模糊搜索
        self.input_value(self.search_element, text='沪TES', context="搜索输入框")
        self.click(self.search_button, context="搜索按钮")
        self.wait(1)
        self.hover(args=self.search_element, context="搜索输入框")
        self.wait(1)
        self.click(args=self.search_value_clear, context="清空按钮")
        self.wait(1)
        # 精确搜索
        self.input_value(self.search_element, text="沪TEST01", context="搜索输入框")
        self.click(self.search_button, context="搜索按钮")
        self.wait(1)
        # 跳转详情页面
        self.click(args=self.car_detail, context="详情")
        self.wait(1)
        self.click(args=self.car_photo, context='车辆照片')
        self.wait(2)

    def car_search_update(self):
        '''
        修改车辆
        :return:
        '''
        self.open(self.url)
        self.wait(3)
        # 精确搜索
        self.input_value(self.search_element, text="沪TEST01", context="搜索输入框")
        self.click(self.search_button, context="搜索按钮")
        self.wait(1)
        self.hover(args=self.search_element, context="搜索输入框")
        self.wait(1)
        self.click(args=self.car_update, context="编辑")
        self.wait(1)
        self.clear_input(args=self.car_brand, context="车辆品牌")
        self.wait(1)
        self.input_value(args=self.car_brand, text="修改后的车辆品牌", context="车辆品牌")
        self.click(args=self.car_update_sure, context='确定')
        self.wait(2)

    def car_detail_delete(self):
        '''
        查询车辆 并删除车辆
        :return:
        '''
        self.open(self.url)
        self.wait(3)
        # 精确搜索
        self.input_value(self.search_element, text="沪TEST01", context="搜索输入框")
        self.click(self.search_button, context="搜索按钮")
        self.wait(1)
        self.hover(args=self.search_element, context="搜索输入框")
        self.wait(1)
        self.click(args=self.car_delete, context="删除")
        self.wait(1)
        self.click(args=self.car_delete_sure, context='确定')
        self.wait(2)


if __name__ == '__main__':
    driver = choose_browser()
    L = LonginPage(driver)
    L.login('kobeAdmin002', 'kobe8888')
    case = CarList(driver)
    case.car_detail_delete()
