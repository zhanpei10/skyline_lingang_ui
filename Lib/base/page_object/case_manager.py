# 事件管理页面操作
from Lib.base.keywords import KeyWords
from selenium.webdriver.common.by import By
from Lib.common.common_function import *
from Lib.base.page_object.login_page import LonginPage


class CaseManager(KeyWords):
    '''
    事件管理页面相关的操作
    '''
    url = KeyWords.url + 'event-management/list'
    # 相关元素的定位
    # 事件来源
    case_from = (By.XPATH, '//span[text()="事件来源"]/../span[2]/div/div/span/span/i')
    case_from_choose = (By.XPATH, '//span[text()="AIOT感知"]')
    case_from_sure = (By.XPATH, '//body/div[3]/div/div[3]/button[2]')

    # 选择事件类型进行筛选
    case_type = (By.XPATH, '//input[@placeholder = "请选择事件类型"]')
    case_type_value = (By.XPATH, '//span[text()="规划"]/../label/span/span')
    case_type_sure = (By.XPATH, '//body/div[3]/div/div/button[3]/span')

    # 事件阶段筛选事件
    case_stage = (
        By.XPATH, '/html/body/div[1]/div[1]/main/div/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/span[2]/div/div/input')
    case_stage_type = (By.XPATH, '//span[@class="rz-checkbox__label" and text()="受理"]/../span/span')
    case_stage_sure = (By.XPATH, '//body/div[3]/div/div[3]/button[2]')

    # 事件状态查看事件
    case_status = (By.XPATH, '//span[@class="checkboxpicker_statuses"]//input[@placeholder="请输入"]')
    case_status_value = (By.XPATH, '//body/div[3]/div/div[2]/div/label[1]/span[1]/span')
    case_status_sure = (By.XPATH, '//body/div[3]/div/div[3]/button[2]')

    # 事发时间查看事件
    case_find_time1 = (By.XPATH, '//div[@class="top"]//span[text()="事发时间"]/../div//span[text()="近7天"]')
    case_find_time2 = (By.XPATH, '//div[@class="top"]//span[text()="事发时间"]/../div//span[text()="近15天"]')
    case_find_time3 = (By.XPATH, '//div[@class="top"]//span[text()="事发时间"]/../div//span[text()="不限"]')
    # 根据事发地点搜索事件
    case_find_by_address = (By.XPATH, '//input[@placeholder="请输入事件编号或事发地点"]')
    case_find_click = (By.XPATH, '//input[@placeholder="请输入事件编号或事发地点"]/../../../div[2]/i')
    case_find_clear = (By.XPATH, '//input[@placeholder="请输入事件编号或事发地点"]/../span//i')

    # 点击紧急待办 超期未办 正常 所有
    case_urgency = (By.XPATH, '//span[text()="紧急待办"]')
    case_overdue = (By.XPATH, '//span[text()="超期未办"]')
    case_correct = (By.XPATH, '//span[text()="正常"]')
    case_all = (By.XPATH, '//span[text()="所有"]')

    # 排序
    case_sort_by_find_time_desc = (By.XPATH, '//thead//div[text()="事发时间"]/span/i[2]')
    case_sort_by_find_time_asc = (By.XPATH, '//thead//div[text()="事发时间"]/span/i[1]')
    case_sort_by_times_asc = (By.XPATH, '//thead//div[text()="违法次数"]/span/i[1]')
    case_sort_by_times_desc = (By.XPATH, '//thead//div[text()="违法次数"]/span/i[2]')
    case_sort_by_update_time_asc = (By.XPATH, '//thead//div[text()="更新时间"]/span/i[1]')
    case_sort_by_update_time_desc = (By.XPATH, '//thead//div[text()="更新时间"]/span/i[2]')

    # 查看事件详情接口测试
    look_detail = (By.XPATH, '//tbody/tr[1]/td[12]//span')
    look_detail_basic = (By.XPATH, '//div[contains(text(), "基本信息")]')
    look_detail_map = (By.XPATH, '//div[contains(text(), "电子地图")]')
    look_detail_process = (By.XPATH, '//div[contains(text(), "执法全过程")]')
    look_detail_return = (By.XPATH, '//div[@class="btnbar"]//button[1]/span[text()="返回"]')

    # 查看已处理、 已过期、 未配置流程事件
    look_already = (By.XPATH, '//div[contains(text(), "已处理")]')
    look_overdue = (By.XPATH, '//div[contains(text(), "已过期")]')
    look_pending = (By.XPATH, '//div[contains(text(), "待处理")]')
    look_un_configure = (By.XPATH, '//div[contains(text(), "未配置流程")]/span')

    def look_by_case_from(self):
        '''
        根据事件来源查询事件
        :return:
        '''
        self.open(url=self.url)
        self.wait(3)
        self.click(args=self.case_from, context='事件来源')
        self.wait(1)
        self.click(args=self.case_from_choose, context='全部')
        self.wait(1)
        self.click(args=self.case_from_sure, context='确认')
        self.wait(2)

    def look_by_case_type(self):
        '''
        根据事件类型筛选事件
        :return:
        '''
        self.open(url=self.url)
        self.wait(3)
        self.click(args=self.case_type, context='事件类型')
        self.click(args=self.case_type_value, context='规划')
        self.wait(1)
        self.click(args=self.case_type_sure, context='确认')
        self.wait(3)

    def look_by_case_stage(self):
        '''
        根据事件阶段筛选事件
        :return:
        '''
        self.open(url=self.url)
        self.wait(2)
        self.hover(args=self.case_stage, context='事件阶段')
        self.wait(1)
        self.click(args=self.case_stage, context='事件阶段')
        # self.js_click(args=self.case_stage, context='事件阶段')
        self.wait(2)
        self.click(args=self.case_stage_type, context='受理')
        self.wait(1)
        self.click(args=self.case_stage_sure, context='确认')
        self.wait(3)

    def look_by_case_status(self):
        '''
        根据事件状态查看事件
        :return:
        '''
        self.open(url=self.url)
        self.wait(3)
        self.click(args=self.case_status, context='事件状态')
        self.wait(1)
        self.click(args=self.case_status_value, context='已上报')
        self.wait(1)
        self.click(args=self.case_status_sure, context='确认')
        self.wait(2)

    def look_by_case_time_and_keyword(self):
        '''
        根据事件时间查看事件列表
        '''
        self.open(url=self.url)
        self.wait(2)
        self.click(args=self.case_find_time1, context='近7天')
        self.wait(1)
        self.click(args=self.case_find_time2, context='近15天')
        self.wait(1)
        self.click(args=self.case_find_time3, context='不限')
        self.wait(1)
        self.click(args=self.case_find_by_address, context='搜索框')
        self.input_value(args=self.case_find_by_address, text='上海', context='搜索框')
        self.wait(2)
        self.click(args=self.case_find_click, context='搜索按钮')
        self.wait(2)
        # self.hover(args=self.case_find_by_address, context='搜索框')
        # self.hover(args=self.case_find_clear, context='清空')
        # self.click(args=self.case_find_clear, context='清空')
        # self.wait(2)

    def look_by_case_urgency_sort(self):
        '''
        根据点击紧急待办 超期未办 正常 所有 查看事件 然后排序
        :return:
        '''
        self.open(self.url)
        self.wait(1)
        self.click(args=self.case_urgency, context='紧急待办')
        self.wait(2)
        self.click(args=self.case_overdue, context='超期未办')
        self.wait(2)
        self.click(args=self.case_correct, context='正常')
        self.wait(2)
        self.click(args=self.case_all, context='全部')
        self.wait(2)
        # 根据事发时间进行排序
        self.click(args=self.case_sort_by_find_time_asc, context='事发时间升序')
        self.wait(2)
        self.click(args=self.case_sort_by_find_time_desc, context='事发时间降序')
        self.wait(2)
        # 根据违法次数进行排序
        self.click(args=self.case_sort_by_times_asc, context='违法次数升序')
        self.wait(2)
        self.click(args=self.case_sort_by_times_desc, context='违法次数降序')
        self.wait(2)
        # 根据更新时间进行排序
        self.click(args=self.case_sort_by_update_time_asc, context='修改时间升序')
        self.wait(2)
        self.click(args=self.case_sort_by_update_time_desc, context='修改时间降序')
        self.wait(2)

    def look_case_detail(self):
        '''
        查看事件详情接口测试
        :return:
        '''
        self.open(self.url)
        self.wait(2)
        self.click(args=self.look_detail, context='查看详情')
        self.wait(3)
        self.click(args=self.look_detail_map, context='电子地图')
        self.wait(2)
        self.click(args=self.look_detail_basic, context='基本信息')
        self.wait(2)
        self.click(args=self.look_detail_process, context='执法全过程')
        self.wait(2)

    def look_case_already(self):
        '''
        # 查看已处理、 已过期、 未配置流程事件
        :return:
        '''
        self.open(self.url)
        self.wait(2)
        self.click(args=self.look_already, context='已处理')
        self.wait(2)
        self.click(args=self.look_overdue, context='已过期')
        self.wait(2)
        self.click(args=self.look_pending, context='待处理')
        self.wait(2)
        self.click(args=self.look_un_configure, context='未配置流程事件')
        self.wait(1)


if __name__ == '__main__':
    driver = choose_browser()
    L = LonginPage(driver)
    L.login('kobeAdmin002', 'kobe8888')
    case = CaseManager(driver)
    case.look_case_already()
