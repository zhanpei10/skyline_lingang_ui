'''
日志生成文件
'''
import configparser
# from Config.log_dict import LOGGING_DIC
from logging import config
import logging
import os
import time


# def set_log_path(log_type):
#     '''
#     获取日志的存放路径
#     :param log_type:  日志级别
#     :return:
#     '''
#     base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))  # log文件的目录
#     log_dir = os.path.join(base_dir, 'Log', log_type)
#     if not os.path.exists(log_dir):
#         os.mkdir(log_dir)
#     log_name = time.strftime('%Y%m%d') + '_ui_auto_case.log'
#     # 设置日志配置文件当中的日志路径
#     log_dict.LOG_DIR = os.path.join(log_dir, log_name)
#     return log_dir


def error_log():
    '''
    根据日志字典，配置日志格式
    :return: 
    '''
    from Config import log_dict
    log_dict.set_log_path('error_log')
    config.dictConfig(log_dict.get_logging_dic())
    logger = logging.getLogger('UITEST')
    return logger


def normal_log():
    '''
    普通日志
    :return:
    '''
    # 设置配置文件路径
    from Config import log_dict
    log_dict.set_log_path('normal_log')
    config.dictConfig(log_dict.get_logging_dic())
    logger = logging.getLogger('UITEST')
    return logger


if __name__ == '__main__':
    print()
    print(set_log_path('normal_log'))
    print(log_dict.LOG_DIR)
