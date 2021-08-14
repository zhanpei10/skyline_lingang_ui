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


    def add_meeting(self):
        '''
        新建会议，先将会议添加到草稿箱，再添加
        :return:
        '''


if __name__ == '__main__':


