# from Lib.base.keywords import KeyWords
from selenium import webdriver
from Lib.common.chrome_options import Options


def my_test1():
    drvier = webdriver.Chrome(options=Options().my_chrome_options())
    drvier.get('http://www.baidu.com')


if __name__ == '__main__':
    my_test1()
