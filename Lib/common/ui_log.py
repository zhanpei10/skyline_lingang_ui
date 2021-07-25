'''
日志生成文件
'''
import configparser
from Config.log_dict import LOGGING_DIC
from logging import config
import logging


def log():
    '''
    根据日志字典，配置日志格式
    :return: 
    '''
    config.dictConfig(LOGGING_DIC)
    logger = logging.getLogger('UITEST')
    return logger


if __name__ == '__main__':
    log().info('这是一条测试日志')
