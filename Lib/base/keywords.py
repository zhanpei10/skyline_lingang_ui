'''
添加页面操作关键字
'''
from selenium import webdriver
from Lib.common.chrome_options import Options
from Lib.common.ui_log import log
from selenium.webdriver.support.wait import WebDriverWait


def choose_browser(browser_type):
    '''
    根据浏览器类型打开浏览器
    :param browser_type:
    :return:
    '''
    if browser_type == 'chrome':
        log().info('>>>正在加载{0}驱动'.format(browser_type))
        return webdriver.Chrome(Options().my_chrome_options())
    elif browser_type == 'firefox':
        log().info('>>>正在加载{0}驱动'.format(browser_type))
        return webdriver.Firefox()
    elif browser_type == 'ie':
        log().info('>>>正在加载{0}驱动'.format(browser_type))
        return webdriver.Ie()
    else:
        log().info('>>>正在加载{0}驱动'.format('chrome'))
        return webdriver.Chrome(Options().my_chrome_options())


class KeyWords:
    '''
      页面元素相关操作的封装
    '''
    # driver = webdriver.Chrome()

    def __init__(self, browser_type):
        self.driver = choose_browser(browser_type)

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
        设置显示等待
        try:
            log().info('>>>查找元素{0}开始'.format(context))
            element = WebDriverWait(self.driver, 10, 0.5).until(
                lambda el1: self.driver.find_element(*args), message='要找的元素没找到'
            )
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
            log().info('>>>为{0}输入值开始'.format(context))
            self.locator(args, context).send_keys(text)
        except Exception as e:
            log().debug('{0}输入值失败'.format(context))
            self.quite()

    def click(self, args, context=None):
        '''
        点击某个元素
        :param args:
        :param context:
        :return:
        '''
        try:
            log().info('>>>为{0}输入值开始'.format(context))
            self.locator(args, context).click()
        except Exception as e:
            log().debug('{0}点击失败'.format(context))
            self.quite()
