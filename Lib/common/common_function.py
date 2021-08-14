# 添加常用的公共函数
import configparser
import os
from selenium import webdriver
from Lib.common.chrome_options import Options
from Lib.common.ui_log import error_log, normal_log


# 获取项目的根路径
def get_path():
    return os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


# 读取配置文件信息，获得环境地址
def get_url(environment, key):
    '''

    :param environment:  对应的环境
    :param key:  环境下的配置
    :return:
    '''
    conf = configparser.ConfigParser()
    conf.read(get_path() + '/Config/environment.ini')
    return conf.get(environment.upper(), key)


# 读取mysql配置信息
def get_mysql_config(environment):
    '''

    :param environment:  环境信息
    :return: 配置字典
    '''
    # 定义配置字典
    config_dict = {
        'host': None,
        'port': None,
        'user': None,
        'passwd': None,
        'charset': None,
        'database': None,
    }
    # 读取配置文件
    conf = configparser.ConfigParser()
    conf.read(get_path() + '/Config/mysql_config.ini')
    # 给配置字典赋值
    for key in config_dict.keys():
        if key == 'port':
            config_dict[key] = int(conf.get(environment.upper(), key))
        else:
            config_dict[key] = conf.get(environment.upper(), key)
    return config_dict


# 选择浏览器
# 当前选择的浏览器为chrome 可根据需要进行修改
def choose_browser(browser_type=''):
    '''
    根据浏览器类型打开浏览器
    :param browser_type:
    :return:
    '''
    if browser_type == 'chrome':
        normal_log().info('>>>正在加载{0}驱动'.format(browser_type))
        return webdriver.Chrome(options=Options().my_chrome_options())
    elif browser_type == 'firefox':
        normal_log().info('>>>正在加载{0}驱动'.format(browser_type))
        return webdriver.Firefox()
    elif browser_type == 'ie':
        normal_log().info('>>>正在加载{0}驱动'.format(browser_type))
        return webdriver.Ie()
    else:
        normal_log().info('>>>正在加载{0}驱动'.format('chrome'))
        return webdriver.Chrome(options=Options().my_chrome_options())


if __name__ == '__main__':
    print(get_mysql_config('SIT_MYSQL'))
