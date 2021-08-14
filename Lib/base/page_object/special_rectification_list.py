'''
专项整治列表页面
'''
from Lib.base.keywords import KeyWords
from selenium.webdriver.common.by import By
from Lib.common.common_function import *
from Lib.base.page_object.login_page import LonginPage


class SpecialRectificationList(KeyWords):
    '''
    专项整治类
    '''
    url = KeyWords.url + 'special-rectification/list'

    # 专项整治筛选
    # 1、 分类
    classify = (By.XPATH, '//form/div[1]//input')  # 分类下拉框
    classify_value = (By.XPATH, '//body/div[2]/div[1]/div[1]/ul/li[2]/span')  # 具体分类
    classify_bx = (By.XPATH, '//body//div[2]//span[@title="不限"]')  # 不限
    # 2、 状态
    status = (By.XPATH, '//form/div[2]/div/div//input')  # 状态下拉框
    status_values = (By.XPATH, '//ul/li/span[text()="方案制定"]')  # 状态
    status_bx = (By.XPATH, '//body/div[3]//ul/li[1]/span')  # 不限
    # 3、 输入名称
    search_name = (By.XPATH, '//input[@placeholder="请输入名称"]')  # 输入框
    search_button = (By.XPATH, '//input[@placeholder="请输入名称"]/../../../div[2]/i')  # 搜索按钮
    # 收藏按钮点击
    collection_only_button = (By.XPATH, '//span[text()="只看收藏"]/../span/span')

    # 查看专项整治详情
    url_img = (By.XPATH, '//div[@class="list-view-content"]/div[1]/div[1]//img')
    work_log = (By.XPATH, '//div[@id="tab-log"]')  # 工作日志
    work_list = (By.XPATH, '//div[@id="tab-report"]')  # 工作报表
    work_method = (By.XPATH, '//div[@id="tab-detail"]')  # 工作方案
    update_button = (By.XPATH, '//span[text()="编辑"]')  # 点击编辑
    # 修改装修整治的内容
    aim_input = (By.XPATH, '//textarea[@placeholder="请输入整治方案目的"]')
    update_work_method = (By.XPATH, '//div[text()="工作方案"]')  # 修改页面工作方案
    update_sure = (By.XPATH, '//span[text()="确认"]')

    # 专项整治流转
    task_issued_by = (By.XPATH, '//span[text()="任务下发"]')  # 任务下发
    send_user = (By.XPATH, '//span[text()="请选择发送人员"]')  # 发送人员
    send_user_value = (By.XPATH, '//body/div[2]//ul/li[3]/label/span/span')  # 选择要发送的人
    send_user_sure = (By.XPATH, '//body/div[2]//span[text()="确定"]')  # 选择确定
    flow = (By.XPATH, '//span[text()="流转"]')  # 事件流转

    # 添加工作日志
    go_add = (By.XPATH, '//main//span[text()="去添加"]')  # 去添加
    template_name = (By.XPATH, '//label[text()="模板名称"]/../div/div/input')  # 模板名称
    upload_click = (By.XPATH, '//span[text()="上传模板"]')  # 上传模板
    next_step = (By.XPATH, '//span[text()="下一步"]')
    # 选择需要添加的人员
    need_people = (By.XPATH, '//span[text()="请选择需要提交人员"]')
    need_people_value = (By.XPATH, '//body/div[3]//ul/li[3]/label/span/span')
    need_people_sure = (By.XPATH, '//body/div[3]//span[text()="确定"]')
    # 选择需要查看的人
    look_people = (By.XPATH, '//body/div[1]//span[text()="请选择可以查看人员"]')
    look_people_value = (By.XPATH, '//body/div[4]//ul/li[3]/label/span/span')
    look_people_sure = (By.XPATH, '//body/div[4]//span[text()="确定"]')

    # 选择时间
    start_time = (By.XPATH, '//input[@placeholder="开始日期"]')
    end_time = (By.XPATH, '//input[@placeholder="结束日期"]')
    save_time = (By.XPATH, '//label[text() ="统计规则"]')
    # 点击确认
    work_log_sure = (By.XPATH, '//main/div/div[2]/div[2]/div/div[2]/div/form[2]/div[5]/button[3]/span')

    def special_rectification_filter(self):
        '''
        专项整治筛选相关的功能测试
        :return:
        '''
        self.open(self.url)
        # 根据分类进行筛选
        self.wait(2)
        self.click(args=self.classify, context='分类下拉框')
        self.wait(1)
        self.click(args=self.classify_value, context='分类的具体值')
        self.wait(2)
        self.click(args=self.classify, context='分类下拉框')
        self.wait(1)
        self.click(args=self.classify_bx, context='不限')
        self.wait(2)
        # 根据状态进行筛选
        self.click(args=self.status, context='状态下拉框')
        self.wait(1)
        self.click(args=self.status_values, context='方案制定')
        self.wait(2)
        self.click(args=self.status, context='状态下拉框')
        self.wait(1)
        self.click(args=self.status_bx, context='不限')
        self.wait(2)
        #  使用关键字进行搜索
        self.click(args=self.search_name, context='搜索框')
        self.input_value(self.search_name, text='专项整治', context='搜索框')
        self.click(self.search_button, context='搜索按钮')
        self.wait(2)
        # 点击收藏按钮
        self.click(self.collection_only_button, context='只看收藏')
        self.wait(1)
        self.click(self.collection_only_button, context='只看收藏')
        self.wait(2)
        # 添加工作日志

    def special_rectification_detail_and_update(self):
        '''
        查看专项整治详情
        :return:
        '''
        self.open(self.url)
        self.click(2)
        self.click(args=self.url_img, context='专项整治封面')
        self.wait(2)
        self.click(args=self.work_log, context='工作日志')
        self.wait(1)
        self.click(args=self.work_list, context='工作报表')
        self.wait(1)
        self.click(args=self.work_method, context='工作方案')
        self.wait(1)
        self.click(args=self.update_button, context='编辑')
        self.wait(2)
        # 编辑页面输入内容
        # 拖动页面到目的
        self.drag_up_and_down(args=self.aim_input, context="目的输入框")
        self.wait(1)
        self.clear_input(args=self.aim_input, context='目的输入框')
        self.wait(1)
        self.input_value(args=self.aim_input, text='这是编辑之后的目的', context='目的输入框')
        self.wait(1)
        self.click(args=self.update_work_method, context='工作方案')
        self.wait(1)
        self.click(args=self.update_sure, context='确认')
        self.wait(2)

    def special_rectification_detail_flow(self):
        '''
        查看详情并流转
        :return:
        '''
        self.open(self.url)
        self.click(2)
        self.click(args=self.url_img, context='专项整治封面')
        self.wait(1)
        self.click(args=self.task_issued_by, context='任务下发')
        self.wait(1)
        self.click(args=self.send_user, context="发送人员")
        self.wait(1)
        self.click(args=self.send_user_value, context='发送人')
        self.wait(1)
        self.click(args=self.send_user_sure, context='确定')
        self.wait(2)
        self.click(args=self.flow, context='流转')
        self.wait(2)

    def special_rectification_add_work_log(self):
        '''
        添加工作日志
        :return:
        '''
        self.open(url=self.url)
        self.wait(2)
        self.click(args=self.url_img, context='专项整治封面')
        self.click(args=self.work_log, context='工作日志')
        self.wait(1)
        self.click(args=self.go_add, context='去添加')
        # 添加日志
        self.wait(1)
        self.input_value(args=self.template_name, text='测试新建的模板名称', context='模板名称')
        # 上传附件
        self.upload_by_exe(args=self.upload_click, context="上传模板")
        self.wait(1)
        self.click(args=self.next_step, context='下一步')
        # 选择需要添加的人员
        self.click(args=self.need_people, context='需要提交的人')
        self.click(args=self.need_people_value, context="选择对应的人")
        self.click(args=self.need_people_sure, context='点击确定')
        # 选择需要查看人
        self.click(args=self.look_people, context='需要查看的人')
        self.click(args=self.look_people_value, context='需要查看的对应的人')
        self.click(args=self.look_people_sure, context='点击确定')
        # 选择时间
        self.input_value(args=self.start_time, text=get_time('%Y-%m-%d', 2), context='输入开始时间')
        self.wait(1)
        self.input_value(args=self.end_time, text=get_time('%Y-%m-%d', 3), context='输入结束时间')
        self.wait(1)
        self.click(args=self.save_time, context='保存时间')
        self.wait(1)
        self.click(args=self.work_log_sure, context='确定')
        self.wait(2)


if __name__ == '__main__':
    driver = choose_browser()
    L = LonginPage(driver)
    L.login('kobeAdmin002', 'kobe8888')
    case = SpecialRectificationList(driver)
    case.special_rectification_add_work_log()
