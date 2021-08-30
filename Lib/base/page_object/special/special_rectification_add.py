'''
新增专项整治
'''
from Lib.base.keywords import KeyWords
from selenium.webdriver.common.by import By
from Lib.common.common_function import *
from Lib.base.page_object.login_page import LonginPage
import uuid
import random


class SpecialRectificationAdd(KeyWords):
    '''
    专项整治类
    '''
    url = KeyWords.url + 'special-rectification/create'

    # 新增专项整治
    # 基本信息
    # 标题和分类
    title = (By.XPATH, '//input[@placeholder = "请输入标题"]')  # 标题
    classify = (By.XPATH, '//input[@placeholder = "请选择分类"]')  # 分类
    classify_value = (By.XPATH, '//body/div[2]//ul/li[1]')  # 具体的分类
    # 开始日期和结束日期
    start_date = (By.XPATH, '//form//input[@placeholder ="开始日期"]')
    end_date = (By.XPATH, '//form//input[@placeholder ="结束日期"]')
    # 参加单位
    join_unit = (By.XPATH, '//input[@placeholder = "请输入参加单位"]')  # 开始日期
    join_unit_value = (By.XPATH, '//body/div[4]//ul/li[1]')
    join_unit_close = (By.XPATH, '//label[text() = "牵头单位"]')
    # 牵头单位
    leading_unit = (By.XPATH, '//input[@placeholder = "请输入牵头单位"]')
    leading_unit_value = (By.XPATH, '//body/div[5]//ul/li[1]')
    leading_unit_close = (By.XPATH, '//label[text() = "目的"]')
    # 输入目的
    aim = (By.XPATH, '//textarea')
    # 工作方案页面操作
    scheme = (By.XPATH, '//div[text()="工作方案"]')
    scheme_value = (By.XPATH, '//div[@data-placeholder="请输入整治方案正文"]')
    save_to_draft = (By.XPATH, '//span[text() = "保存为草稿"]')

    # 将草稿保存
    draft_value = (By.XPATH, '//main/div/div[2]/div[2]/div[1]/div[1]//img')  # 点击专项整治的草稿
    save_special = (By.XPATH, '//main/div/div[2]/div[2]/button[2]')  # 点击确认按钮

    def add_special_rectification(self):
        '''
        新建专项整治
        :return:
        '''
        self.open(url=self.url)
        # 输入标题和选择分类
        self.input_value(args=self.title, text='专项整治' + str(uuid.uuid4()), context='标题')
        self.click(args=self.classify, context='选择分类')
        self.wait(1)
        self.click(args=self.classify_value, context='分类元素')
        # 输入开始日期和结束日期
        self.input_value(args=self.start_date, text=get_time('%Y-%m-%d %H:%M:%S', 1), context='开始日期')
        self.input_value(args=self.end_date, text=get_time('%Y-%m-%d %H:%M:%S', 30), context='结束日期')
        self.wait(1)
        # 选择参加单位
        self.click(args=self.join_unit, context='参加单位')
        self.wait(1)
        self.click(args=self.join_unit_value, context='具体参加单位')
        self.click(args=self.join_unit_close, context='关闭参加单位')
        # 选择牵头单位
        self.wait(1)
        self.click(args=self.leading_unit, context='牵头单位')
        self.wait(1)
        self.click(args=self.leading_unit_value, context='具体的牵头单位')
        self.click(args=self.leading_unit_close, context='关闭牵头单位')
        # 输入目的
        self.input_value(args=self.aim, text="这是专项整治的目的", context='目的')
        self.wait(1)
        # 跳转工作方案页面
        self.click(args=self.scheme, context='工作方案')
        self.wait(2)
        self.input_value(args=self.scheme_value, text='这是工作方案的正文', context='工作方案内容')
        self.wait(1)
        self.click(args=self.save_to_draft, context='保存为草稿')
        self.wait(2)
        # 将草稿箱当中的内容保存
        self.click(args=self.draft_value, context='操作箱当中的专项整治')
        self.wait(2)
        self.click(args=self.save_special, context='确认')
        self.wait(2)


if __name__ == '__main__':
    driver = choose_browser()
    L = LonginPage(driver)
    L.login('kobeAdmin002', 'kobe8888')
    case = SpecialRectificationAdd(driver)
    case.add_special_rectification()
