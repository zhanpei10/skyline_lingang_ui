'''
会议列表页面测试
'''
from Lib.base.keywords import KeyWords
from selenium.webdriver.common.by import By
from Lib.common.common_function import *
from Lib.base.page_object.login_page import LonginPage


class MeetingList(KeyWords):
    '''
    会议列表接口测试
    '''
    url = KeyWords.url + 'meeting-management/list'
    # 根据时间进行筛选
    time_seven = (By.XPATH, '//span[text()="近7天"]')
    time_fifteen = (By.XPATH, '//span[text()="近15天"]')
    time_unlimited = (By.XPATH, '//span[text()="不限"]')
    # 打开时间筛选框
    time_choose = (By.XPATH, '//form//input[@placeholder="开始时间"]')  # 时间输入下拉框
    start_date = (By.XPATH, '//input[@placeholder="开始日期"]')
    # start_time = (By.XPATH, '//input[@placeholder="开始时间" and @class="rz-input__inner"]')
    end_date = (By.XPATH, '//input[@placeholder="结束日期"]')
    date_sure = (By.XPATH, '//div[@class="rz-picker-panel__footer"]//span[text()="确定"]')
    # 根据发布人进行筛选
    issuer = (By.XPATH, '//input[@placeholder="不限"]')
    issuer_value = (By.XPATH, '//section/div[2]/div[3]/div[1]/div')
    # 清空筛选项
    issuer_clear = (By.XPATH, '//input[@placeholder="不限"]/../span/span/i')

    '''--------------------------------------------------------------------'''
    # 查看详情操作
    meeting_detail = (By.XPATH, '//table[@class="rz-table__body"]/tbody/tr[1]//span[text()="详情"]')
    # 编辑会议
    meeting_update_button = (By.XPATH, '//span[text()="编辑"]')
    # 编辑会议内容
    update_title = (By.XPATH, '//input[@placeholder="请输入会议主题"]')
    update_address = (By.XPATH, '//input[@placeholder="请输入会议地点"]')
    update_sure = (By.XPATH, '//main/div[1]/div[2]/div[1]//span[text()="确定"]')

    '''--------------------------------------------------------------------'''
    # 取消会议通知
    cancel_meeting_button = (By.XPATH, '//table[@class="rz-table__body"]/tbody/tr[1]//span[text()="取消会议"]')
    cancel_meeting_sure = (By.XPATH, '//div[@class="rz-message-box"]/div[3]/button[2]/span')

    def list_screen(self):
        '''
        会议记录筛选
        :return:
        '''
        self.open(self.url)

        # 点击固定的时间
        self.wait(2)
        # 自定义时间进行筛选
        self.click(args=self.time_choose, context='时间输入框')
        self.wait(1)
        self.input_value(args=self.start_date, text=get_time('%Y-%m-%d', -15), context='开始日期')
        self.clear_input(args=self.end_date, context='开始日期')
        self.input_value(args=self.end_date, text=get_time('%Y-%m-%d'), context='结束日期')
        self.wait(1)
        # 选择固定的时间
        self.click(args=self.date_sure, context='确认')
        self.wait(1)
        self.click(args=self.time_seven, context='近7天')
        self.wait(1)
        self.click(args=self.time_fifteen, context='近15天')
        self.wait(1)
        self.click(args=self.time_unlimited, context='不限')
        self.wait(1)
        # 根据发布人进行筛选
        self.click(args=self.issuer, context='发布人')
        self.wait(2)
        self.click(args=self.issuer_value, context='具体的发布人')
        self.wait(1)
        # 清空发布人
        self.hover(args=self.issuer, context='发布人')
        self.wait(1)
        self.click(args=self.issuer_clear, context='清空')
        self.wait(2)

    def look_detail_update(self):
        '''
        查看会议详情、修改会议详情、取消会议操作
        :return:
        '''
        self.open(self.url)
        self.wait(1)
        # 查看会议详情
        self.click(args=self.meeting_detail, context='会议详情')
        self.wait(1)
        # 进入编辑页面
        self.click(args=self.meeting_update_button, context='编辑')
        self.wait(3)
        # 填写数据 先删除再编辑
        self.clear_input(args=self.update_title, context='会议主题')
        self.input_value(args=self.update_title, text="这是编辑之后的会议主题", context='会议主题')
        self.clear_input(args=self.update_address, context='会议地址')
        self.input_value(args=self.update_address, text="这是编辑之后的会议地址", context='会议地址')
        self.click(args=self.update_sure, context='确定')
        self.wait(2)

    def cancel_meeting(self):
        '''
        取消会议通知
        :return:
        '''
        self.open(self.url)
        self.wait(2)
        self.click(args=self.cancel_meeting_button, context='取消会议')
        self.wait(1)
        self.click(args=self.cancel_meeting_sure, context='确认')
        self.wait(2)


if __name__ == '__main__':
    driver = choose_browser()
    L = LonginPage(driver)
    L.login('kobeAdmin002', 'kobe8888')
    case = MeetingList(driver)
    case.cancel_meeting()
