'''
车辆管理: 新增车辆
'''
from Lib.base.keywords import KeyWords
from selenium.webdriver.common.by import By
from Lib.common.common_function import *
from Lib.base.page_object.login_page import LonginPage


class CarAdd(KeyWords):
    '''
    新增车辆页面
    '''
    url = KeyWords.url + 'vehicle-center/create'
    # 新增车辆相关元素
    car_number = (By.XPATH, '//input[@placeholder = "请输入车牌号码"]')  # 车牌号码
    car_numbering = (By.XPATH, '//input[contains(@placeholder,"请输入车辆编号")]')  # 车牌编号
    car_brand = (By.XPATH, '//input[@placeholder = "请输入车辆品牌"]')
    choose_org = (By.XPATH, '//input[@placeholder = "请选择使用部门"]')
    org_value = (By.XPATH, '//body/div[2]//ul/li[1]/span')  # 具体的部门
    people_number = (By.XPATH, '//input[@placeholder = "请输入乘坐人数"]')
    # 日期相关
    buy_time = (By.XPATH, '//input[@placeholder = "请选择购置日期"]')
    buy_time_sure = (By.XPATH, '//label[text()="购置日期"]')  # 购置日期
    annual = (By.XPATH, '//input[@placeholder="请选择年审日期"]')
    annual_sure = (By.XPATH, '//label[text()="年审日期"]')
    # 行驶证相关
    car_license = (By.XPATH, '//input[@placeholder = "请输入行驶证编号"]')
    car_license_end_date = (By.XPATH, '//input[@placeholder = "请选择行驶证到期时间"]')
    car_license_end_date_sure = (By.XPATH, '//label[text()="行驶证到期时间"]')
    # 运输证编号
    car_license_id = (By.XPATH, '//input[@placeholder = "请输入运输证编号"]')
    car_license_id_end_date = (By.XPATH, '//input[@placeholder = "请选择运输证到期时间"]')
    car_license_id_end_date_sure = (By.XPATH, '//label[text()="运输证到期时间"]')
    # 上传车辆照片
    car_photo = (By.XPATH, '//span[text()="车辆照片"]')
    car_photo_up = (By.XPATH, '//h3[text()="正前方"]/..//input[@name = "file"]')
    car_photo_down = (By.XPATH, '//h3[text()="正后方"]/..//input[@name = "file"]')
    car_photo_left = (By.XPATH, '//h3[text()="正左侧"]/..//input[@name = "file"]')
    car_photo_right = (By.XPATH, '//h3[text()="正右侧"]/..//input[@name = "file"]')
    car_photo_license = (By.XPATH, '//h3[text()="车辆行驶证"]/..//input[@name = "file"]')
    # 点击新建
    car_create = (By.XPATH, '//span[text()="新建"]')

    def car_add(self):
        '''
        新增车辆
        :return:
        '''
        self.open(self.url)
        self.wait(3)
        self.input_value(args=self.car_number, text='沪TEST01', context="车牌号")
        self.input_value(args=self.car_numbering, text=1234, context="车辆编号")
        self.input_value(args=self.car_brand, text="测试品牌", context="车辆品牌")
        self.click(args=self.choose_org, context='使用部门')
        self.wait(1)
        self.click(args=self.org_value, context="选择的部门")
        self.input_value(args=self.people_number, text=3, context="乘坐人数")
        self.input_value(args=self.buy_time, text=get_time("%Y-%m-%d", -10), context="请选择购置日期")
        self.click(args=self.buy_time_sure, context="购置日期")
        self.input_value(args=self.annual, text=get_time("%Y-%m-%d", 10), context="年审日期")
        self.click(args=self.annual_sure, context="年审日期")
        # 行驶证相关
        self.input_value(args=self.car_license, text=12345678, context="行驶证编号")
        self.input_value(args=self.car_license_end_date, text=get_time('%Y-%m-%d', 300), context="行驶证到期时间")
        self.click(args=self.car_license_end_date_sure, context="行驶证到期时间")
        # 运输证相关
        self.input_value(args=self.car_license_id, text=12345678, context="运输证编号")
        self.input_value(args=self.car_license_id_end_date, text=get_time('%Y-%m-%d', 360), context='运输证到期时间')
        self.click(args=self.car_license_id_end_date_sure, context="运输证到期时间")
        # 上传车辆照片
        self.click(args=self.car_photo, context="车辆照片")
        self.wait(1)
        self.upload_file_to_input(args=self.car_photo_up, context="正前方")
        self.upload_file_to_input(args=self.car_photo_down, context="正后方")
        self.upload_file_to_input(args=self.car_photo_left, context="正左侧")
        self.upload_file_to_input(args=self.car_photo_right, context="正右侧")
        self.upload_file_to_input(args=self.car_photo_license, context="车辆行驶证")
        self.wait(1)
        self.click(args=self.car_create, context="新建")
        self.wait(2)


if __name__ == '__main__':
    driver = choose_browser()
    L = LonginPage(driver)
    L.login('kobeAdmin002', 'kobe8888')
    case = CarAdd(driver)
    case.car_add()
