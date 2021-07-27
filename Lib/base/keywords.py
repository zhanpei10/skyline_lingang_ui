'''
添加页面操作关键字
'''
from selenium import webdriver
from Lib.common.chrome_options import Options
from Lib.common.ui_log import log
from selenium.webdriver.support.wait import WebDriverWait
from Lib.common.common_function import *
from time import sleep


class KeyWords:
    '''
      页面元素相关操作的封装
    '''
    # driver = webdriver.Chrome()
    # 获取url，公共连接
    url = get_url('sit', 'sit_lg')

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        '''
        打开网页
        :param url:
        :param context:
        :return:
        '''
        log().info('>>>打开网页{0}'.format(url))
        self.driver.get(url)

    def locator(self, args, context=None):
        '''
        查找元素
        :param context
        :param args:
        :return:
        '''
        # 设置显示等待
        try:
            log().info('>>>查找元素{0}开始'.format(context))
            print('--------------------------------')
            element = WebDriverWait(self.driver, 10, 0.5).until(
                lambda el1: self.driver.find_element(*args), message='{0}元素没找到'.format(context)
            )
            print(element)
            print('--------------------------------')
            return element
        except Exception as e:
            log().debug('》》》查找元素失败')
            self.quite()
            raise e

    def quite(self):
        '''
        关闭浏览器
        :return:
        '''
        log().info('退出浏览器成功')
        self.driver.quit()

    def input_value(self, args, text, context=None):
        '''
        为输入框输入在值
        :param args:
        :param text: 需要输入的值
        :param context:
        :return:
        '''
        try:
            log().info('>>>为{0}元素输入值开始'.format(context))
            self.locator(args, context).send_keys(text)
            print(text)
        except Exception as e:
            log().debug('{0}元素输入值失败'.format(context))
            self.quite()
            raise e

    def click(self, args, context=None):
        '''
        点击某个元素
        :param args:
        :param context:
        :return:
        '''
        try:
            log().info('>>>点击{0}元素'.format(context))
            self.locator(args, context).click()
        except Exception as e:
            log().debug('{0}元素点击失败'.format(context))
            self.quite()
            raise e

    def wait(self, second):
        '''
        设置显示等待
        :return:
        '''
        sleep(second)
