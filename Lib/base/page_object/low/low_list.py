from Lib.base.keywords import KeyWords
from selenium.webdriver.common.by import By
from Lib.common.common_function import *
from Lib.base.page_object.login_page import LonginPage


class LowList(KeyWords):
    url = KeyWords.url + 'laws-center/query'
    # -------------------搜索相关关键字----------------------------
    search_input = (By.XPATH, '//input[@placeholder="请输入关键词"]')
    search_button = (By.XPATH, '//i[contains(@class, "rz-icon-search")]')
    search_clear = (By.XPATH, '//i[contains(@class, "rz-input__clear")]')

    # --------------------查看详情----------------------------------
    look_detail = (By.XPATH, '//tr[@class="rz-table__row"]//span[text()="查看"]')

    # ------------------------修改--------------------------------
    update_button = (By.XPATH, '//tr[@class="rz-table__row"]//span[text()="修改"]')
    # 修改相关的元素
    # 执法分类
    low_fl = (By.XPATH, '//label[text()="执法分类"]/../div[1]//input')
    # 法律法规库
    low_k = (By.XPATH, '//label[text()="法律法规库"]/../div[1]//input')
    # 违法名称
    illegal_name = (By.XPATH, '//label[text()="违法行为名称"]/../div[1]//input')
    # 法律法规规章规定
    low_gd = (By.XPATH, '//label[text()="法律法规规章规定"]/../div[1]//textarea')
    # 法律责任适用条款
    low_tk = (By.XPATH, '//label[text()="法律责任适用条款"]/../div[1]//textarea')
    # 点击新建
    save_update = (By.XPATH, '//span[text()="保存"]')

    # --------------------删除------------------------------
    delete_button = (By.XPATH, '//tr[@class="rz-table__row"]//span[text()="删除"]')
    delete_sure = (By.XPATH, '//div[contains(@x-placement, "top")]//span[text()="确定"]')

    def low_search_and_detail(self):
        '''
        搜索法律法规和查看详情
        :return:
        '''
        self.open(self.url)
        self.wait(2)
        # 模糊搜索
        self.input_value(args=self.search_input, text="自动化", context="搜索法律法规输入框")
        self.click(args=self.search_button, context="搜索按钮")
        self.wait(1)
        # 清空输入框
        self.hover(args=self.search_input, context="搜索法律法规输入框")
        self.click(args=self.search_clear, context="清空按钮")
        # 精确搜索
        self.input_value(args=self.search_input, text="自动化执法分类", context="搜索法律法规输入框")
        self.click(args=self.search_button, context="搜索按钮")
        self.wait(1)
        # 查看法律法规
        self.click(args=self.look_detail, context="查看")
        self.wait(1)

    def low_search_and_update(self):
        '''
        搜索法律法规和编辑
        :return:
        '''
        self.open(self.url)
        self.wait(2)
        # 精确搜索
        self.input_value(args=self.search_input, text="自动化执法分类", context="搜索法律法规输入框")
        self.click(args=self.search_button, context="搜索按钮")
        self.wait(1)
        # 查看法律法规
        self.click(args=self.update_button, context="修改")
        self.wait(1)
        # 修改相关的字段
        # 执法分类
        self.clear_input(args=self.low_fl, context="执法分类")
        self.input_value(args=self.low_fl, text="修改后的自动化执法分类", context="执法分类")
        # 法律法规库
        self.clear_input(args=self.low_k, context="法律法规库")
        self.input_value(args=self.low_k, text="修改后的自动化法律法规库", context="法律法规库")
        # 违法行为名称
        self.clear_input(args=self.illegal_name, context="违法行为名称")
        self.input_value(args=self.illegal_name, text="修改后的自动化违法行为名称", context="违法行为名称")
        # 法律法规规章规定
        self.clear_input(args=self.low_gd, context="法律法规规章规定")
        self.input_value(args=self.low_gd, text="修改后的自动化法律法规规章规定", context="法律法规规章规定")
        # 法律责任适用条款
        self.clear_input(args=self.low_tk, context="法律责任适用条款")
        self.input_value(args=self.low_tk, text="修改后的自动化法律责任适用条款", context="法律责任适用条款")
        # 点击保存
        self.click(args=self.save_update, context="保存")

    def low_search_and_delete(self):
        '''
        搜索法律法规和删除
        :return:
        '''
        self.open(self.url)
        self.wait(2)
        # 精确搜索
        self.input_value(args=self.search_input, text="自动化执法分类", context="搜索法律法规输入框")
        self.click(args=self.search_button, context="搜索按钮")
        self.wait(1)
        # 删除
        self.click(args=self.delete_button, context="删除")
        self.wait(1)
        # 确定
        self.click(args=self.delete_sure, context="确定")
        self.wait(1)


if __name__ == '__main__':
    driver = choose_browser()
    L = LonginPage(driver)
    L.login('kobeAdmin002', 'kobe8888')
    case = LowList(driver)
    case.low_search_and_update()
