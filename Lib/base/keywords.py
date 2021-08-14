'''
添加页面操作关键字
'''
from selenium import webdriver
from Lib.common.chrome_options import Options
from Lib.common.ui_log import error_log, normal_log
# 设置显示等待
from selenium.webdriver.support.wait import WebDriverWait
# 鼠标相关操作
from selenium.webdriver.common.action_chains import ActionChains
from Lib.common.common_function import *
from time import sleep
import time
import os
import sys


class KeyWords:
    '''
      页面元素相关操作的封装
    '''
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
        normal_log().info('>>>打开网页{0}'.format(url))
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
            normal_log().info('>>>查找元素{0}开始'.format(context))
            element = WebDriverWait(self.driver, 10, 0.5).until(
                lambda el1: self.driver.find_element(*args), message='{0}元素没找到'.format(context)
            )
            return element
        except Exception as e:
            error_log().debug('》》》查找元素失败')
            self.get_error_picture(context)
            # self.quite()
            # raise e

    def quite(self):
        '''
        关闭浏览器
        :return:
        '''
        normal_log().info('退出浏览器成功')
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
            normal_log().info('>>>为{0}元素输入值开始'.format(context))
            self.locator(args, context).send_keys(text)
        except Exception as e:
            error_log().debug('{0}元素输入值失败'.format(context))
            error_log().debug('>>>>>>>>>{0}'.format(e))
            self.get_error_picture(context)
            # self.quite()
            # raise e

    def click(self, args, context=None):
        '''
        点击某个元素
        :param args:
        :param context:
        :return:
        '''
        try:
            normal_log().info('>>>点击{0}元素'.format(context))
            self.locator(args, context).click()
        except Exception as e:
            error_log().debug('{0}元素点击失败'.format(context))
            error_log().debug('>>>>>>>>>>>>>>>>>>>{0}'.format(e))
            self.get_error_picture(context)
            # self.quite()
            # raise e

    def wait(self, second):
        '''
        设置显示等待
        :return:
        '''
        sleep(second)

    def click_by_js(self, args, context=None):
        '''
        根据js查找元素，并对
        :param args:
        :param context:
        :return:
        '''
        pass

    def hover(self, args, context=None):
        '''
        设置鼠标悬停
        :param args:
        :param context:
        :return:
        '''
        try:
            normal_log().info('>>>>>>>>>>>>鼠标悬停{0}'.format(context))
            element = self.locator(args, context)
            ActionChains(self.driver).move_to_element(element).perform()
        except Exception as e:
            error_log().debug('鼠标悬停{0}失败'.format(context))
            error_log().debug('>>>>>>>>>>>>>>>>>>>{0}'.format(e))
            self.get_error_picture()
            # self.quite()
            # raise e

    def js_click(self, args, context=None):
        '''
        使用js点击元素
        :param args:
        :param context:
        :return:
        '''
        try:
            normal_log().info('>>>>>>>>>>>>js点击{0}'.format(context))
            element = self.locator(args, context)
            js = 'arguments[0].click()'
            # driver = webdriver.Chrome()
            self.driver.execute_script(js, element)
        except Exception as e:
            error_log().debug('js点击{0}失败'.format(context))
            error_log().debug('>>>>>>>>>>>>>>>>>>>{0}'.format(e))
            self.get_error_picture(context)
            # self.quite()
            # raise e

    def get_text(self, args, context=None):
        '''
        获取元素的文本信息，用作断言
        :param args:
        :param context:
        :return:
        '''
        try:
            normal_log().info('>>>>>>>>>>>获取{}的文本信息'.format(context))
            element = self.locator(args, context)
            return element.text
        except Exception as e:
            error_log().debug('>>>获取{0}文本信息失败'.format())
            error_log().debug('>>>{0}'.format(e))
            self.get_error_picture(context)
            # self.quite()
            # raise e

    def get_error_picture(self, context=None):
        '''
        拍摄错误的图
        :param context: 图片名称
        :return:
        '''
        # 路径拼接
        str_name = time.strftime('%Y%m%d%H%M%S')
        path = get_path() + '/Data/error_picture/{0}{1}.png'.format(str_name, context)
        # driver = webdriver.Chrome()
        self.driver.save_screenshot(path)

    def make_assert_by_text(self, args, assert_data, context=None):
        '''
        根据文本信息设置断言
        :param args:
        :param assert_data:
        :param context:
        :return:
        '''
        try:
            text = self.get_text(args=args, context=context)
            assert assert_data in text, '断言失败，没有获得对应的文本信息'
        except AssertionError as e:
            error_log().debug('>>>>>>{}执行失败'.format(context))
            error_log().debug(e)
            self.get_error_picture(context)
            raise e

    def make_assert_by_compare_time(self, args1, args2, context=None):
        try:
            time1_str1 = self.get_text(args=args1, context=context)
            time1 = time.mktime(time.strptime(time1_str1.strip(), '%Y-%m-%d %H:%M:%S'))
            time1_str2 = self.get_text(args=args2, context=context)
            time2 = time.mktime(time.strptime(time1_str2.strip(), '%Y-%m-%d %H:%M:%S'))
            assert int(time1) > int(time2), '排序错误'
        except AssertionError as e:
            error_log().debug('>>>>>>{}执行失败'.format(context))
            error_log().debug(e)
            self.get_error_picture(context)
            raise e

    def clear_input(self, args, context=None):
        '''
        清空输入框
        :param args:
        :param context:
        :return:
        '''
        try:
            normal_log().info('>>>>>>>>>清空{}输入框'.format(context))
            self.locator(args=args, context=context).clear()
        except Exception as e:
            error_log().debug('>>>>>>清空操作失败')
            error_log().debug(e)
            self.driver.save_screenshot(context)
            self.quite()
            raise e

    def drag_up_and_down(self, args, context=None):
        '''
        上下进行拖动
        :return:
        '''
        try:
            normal_log().info('>>>>>>>>>将鼠标拖动到{}开始'.format(context))
            element = self.locator(args=args, context=context)
            js = "arguments[0].scrollIntoView();"
            self.driver.execute_script(js, element)
        except Exception as e:
            error_log().debug('>>>>>将鼠标拖动到{}失败'.format(context))
            error_log().debug(e)
            self.quite()
            raise e

    def upload_by_exe(self, args, context=None):
        '''
        input元素的附件上传
        :return:
        '''
        try:
            normal_log().info('>>>>>开始上传{}附件'.format(context))
            # 点击附件上传弹窗
            self.click(args=args, context=context)
            self.wait(2)
            # 执行对应的程序
            path = get_path() + '/Resource/file_exe/test.exe'
            os.system(path)
        except Exception as e:
            error_log().debug('>>>上传{}附件失败'.format(context))
            error_log().debug('>>>>>{}'.format(e))
            raise e


if __name__ == '__main__':
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    print(time.strptime('2021-07-26 17:12:52', '%Y-%m-%d %H:%M:%S'))
    print(time.mktime(time.strptime('2021-07-26 17:12:52', '%Y-%m-%d %H:%M:%S')))
