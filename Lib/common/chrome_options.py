# 浏览器相关设置
from selenium import webdriver
from time import sleep

'''
配置ChromeOptions：一般作为一个专门的配置类进行存放
特殊场景下的浏览器配置是需要自行去查找资料的。但是查找的时候要记得看代码：
    新版本：driver = webdriver.Chrome(options=options)
    老版本：driver = webdriver.Chrome(chrome_options=options)
    因为老版本的options配置，配置参数是chrome_options，而新版本的参数是options
常用的浏览器配置项：
    1. 去掉黄条警告
    2. 窗体最大化
    3. 读取本地缓存
    4. 无头模式
    5. 禁用密码管理窗体
'''


class Options:
    '''
    打开浏览器时的相关参数配置
    :return:
    '''

    def my_chrome_options(self):
        '''
        谷歌浏览器参数配置
        :return:
        '''
        options = webdriver.ChromeOptions()
        # 去掉浏览器正在被自动化操作的相关警告
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 窗体最大化设置
        options.add_argument('start-maximized')
        # 去掉密码管理弹窗
        prefs = {}
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enabled"] = False
        options.add_experimental_option("prefs", prefs)
        return options
