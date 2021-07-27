# 登录页面封装
from Lib.base.keywords import KeyWords
from Lib.common.common_function import *
from selenium.webdriver.common.by import By


class LonginPage(KeyWords):
    # 添加登录页面的URL
    url = KeyWords.url
    # 页面元素
    username = (By.XPATH, '//input[@placeholder="请输入用户名"]')
    password = (By.XPATH, '//input[@placeholder="请输入密码"]')
    login_button = (By.XPATH, '//button')

    # 登录操作
    def login(self, user, pw):
        self.open(self.url)
        self.wait(5)
        self.input_value(self.username, user, context='用户名')
        self.input_value(self.password, pw, context='密码')
        self.click(self.login_button, context='登录')


if __name__ == '__main__':
    l = LonginPage(choose_browser())
    user = 'kobeAdmin001'
    pw = 'kobe8888'
    l.login(user, pw)
