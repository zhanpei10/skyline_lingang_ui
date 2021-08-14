# 登录页面封装
from Lib.base.keywords import KeyWords
from Lib.common.common_function import *
from selenium.webdriver.common.by import By


class LonginPage(KeyWords):
    # 添加登录页面的URL
    url = KeyWords.url
    # 登录页面元素
    username = (By.XPATH, '//input[@placeholder="请输入用户名"]')
    password = (By.XPATH, '//input[@placeholder="请输入密码"]')
    login_button = (By.XPATH, '//button')
    # 退出登录元素
    user_self = (By.XPATH, '//body/div/aside/div[3]/div[2]/div/span')
    out = (By.XPATH, '//a[text()="退出"]')

    # 登录操作
    def login(self, user, pw):
        self.open(self.url)
        self.wait(5)
        self.input_value(self.username, user, context='用户名')
        self.input_value(self.password, pw, context='密码')
        self.click(self.login_button, context='登录')
        self.wait(2)

    # 退出登录
    def login_out(self):
        '''
        退出登录操作
        :return:
        '''
        self.hover(args=self.user_self, context='用户名称')
        self.wait(1)
        self.click(args=self.out, context='退出')
        self.wait(2)


if __name__ == '__main__':
    l = LonginPage(choose_browser())
    user = 'kobeAdmin001'
    pw = 'kobe8888'
    l.login(user, pw)
    l.login_out()
