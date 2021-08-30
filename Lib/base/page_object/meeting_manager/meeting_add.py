'''
新增会议管理页面操作
'''
from Lib.base.keywords import KeyWords
from selenium.webdriver.common.by import By
from Lib.common.common_function import *
from Lib.base.page_object.login_page import LonginPage


class MeetingAdd(KeyWords):
    url = KeyWords.url + 'meeting-management/create'
    # 相关元素
    # 会议主题地点
    meeting_title = (By.XPATH, '//input[@placeholder="请输入会议主题"]')
    meeting_address = (By.XPATH, '//input[@placeholder="请输入会议地点"]')
    # 选择参会人员
    join_meeting_button = (By.XPATH, '//main/div/div[2]/form/div[5]//span[@class="join-name"]')
    join_meeting_people = (By.XPATH, '//body/div[2]/div[2]//ul/li[3]/label/span/span')
    join_meeting_sure = (By.XPATH, '//body/div[2]/div[3]/button[3]/span')
    # 附加上传
    file = (By.XPATH, '//span[text()="点击上传"]')
    # 保存为草稿
    save_by_draft = (By.XPATH, '//span[text()="保存为草稿"]')
    # 发送会议
    update = (By.XPATH, '//tbody/tr[1]/td[6]//div/button[1]/span')
    # 发布会议
    meeting_save = (By.XPATH, '//main/div/div[2]/div[1]//span[text()="确定"]')

    def add_meeting(self):
        '''
        新建会议，先将会议添加到草稿箱，再添加
        :return:
        '''
        self.open(self.url)
        self.wait(2)
        # 输入会议标题和会议地址
        self.input_value(args=self.meeting_title, text='这是自动化的会议主题', context='会议主题')
        self.wait(1)
        self.input_value(args=self.meeting_address, text='这是自动化的会议地点', context='会议地点')
        self.wait(1)
        # 选择参会人员
        self.click(args=self.join_meeting_button, context='参会人员下拉框')
        self.wait(2)
        self.click(args=self.join_meeting_people, context='参选人员选择框')
        self.wait(1)
        self.click(args=self.join_meeting_sure, context='确认')
        # 附件上传并保存为草稿
        self.wait(1)
        self.upload_by_exe(args=self.file, context='附件上传')
        self.wait(2)
        self.click(args=self.save_by_draft, context='保存为草稿')
        self.wait(2)
        self.click(args=self.update, context='编辑')
        self.wait(2)
        self.click(args=self.meeting_save, context='发布会议')
        self.wait(2)


if __name__ == '__main__':
    driver = choose_browser()
    L = LonginPage(driver)
    L.login('kobeAdmin002', 'kobe8888')
    case = MeetingAdd(driver)
    case.add_meeting()
