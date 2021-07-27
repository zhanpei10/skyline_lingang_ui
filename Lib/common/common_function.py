# 添加常用的公共函数
import configparser
import os
from selenium import webdriver
from Lib.common.chrome_options import Options
from Lib.common.ui_log import log


# 获取项目的根路径
def get_path():
    return os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


# 读取配置文件信息，获得环境地址
def get_url(environment, key):
    conf = configparser.ConfigParser()
    conf.read(get_path() + '/Config/environment.ini')
    return conf.get(environment.upper(), key)


# 选择浏览器
# 当前选择的浏览器为chrome 可根据需要进行修改
def choose_browser(browser_type=''):
    '''
    根据浏览器类型打开浏览器
    :param browser_type:
    :return:
    '''
    if browser_type == 'chrome':
        log().info('>>>正在加载{0}驱动'.format(browser_type))
        return webdriver.Chrome(options=Options().my_chrome_options())
    elif browser_type == 'firefox':
        log().info('>>>正在加载{0}驱动'.format(browser_type))
        return webdriver.Firefox()
    elif browser_type == 'ie':
        log().info('>>>正在加载{0}驱动'.format(browser_type))
        return webdriver.Ie()
    else:
        log().info('>>>正在加载{0}驱动'.format('chrome'))
        return webdriver.Chrome(options=Options().my_chrome_options())


if __name__ == '__main__':
    print(get_path())
    print(get_url('sit', 'sit_lg'))
