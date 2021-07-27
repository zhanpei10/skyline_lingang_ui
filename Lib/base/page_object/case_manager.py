# 事件管理页面操作
from Lib.base.keywords import KeyWords
from selenium.webdriver.common.by import By
from Lib.common.common_function import *


class CaseManager(KeyWords):
    '''
    事件管理页面相关的操作
    '''
    url = KeyWords.url + '/event-management/list'
    # 相关元素的定位
    # 事件来源
    case_from = (By.XPATH, '//span[text()="事件来源"]/../span[2]//input')
    # 选择事件来源
    case_from_choose = (By.XPATH, '//div[@id="rz-popover-8153"]/div/div[2]//label[1]/span')
    case_from_sure = (By.XPATH, '//span[text()="确认"]/..')

    def look_by_case_from(self):
        self.open(url=self.url)
        self.click(args=self.case_from, context='事件来源')
        self.wait(2)
        self.click(args=self.case_from_choose, context='全部')
        self.wait(1)
        self.click(args=self.case_from_sure, context='确认')


if __name__ == '__main__':
    case = CaseManager(choose_browser())
    case.look_by_case_from()
