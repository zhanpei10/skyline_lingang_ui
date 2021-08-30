# 删除过期的日志和图片
import os
import sys


def delete_log_and_picture(file_date=None):
    '''
    根据时间删除相关的文件
    :param file_date:
    :return:
    '''
    # 获取当前系统的路径
    path = os.path.dirname(os.path.dirname(__file__))
    # 错误日志路径
    error_log_path = path + '/Log/error_log'
    # 普通日志路径
    normal_log_path = path + '/Log/normal_log/'
    # 图片路径
    picture_path = path + '/Data/error_picture'
    # 等于None删除全部
    if file_date is not None:
        # 删除错误的日志
        for i in os.listdir(error_log_path):
            if file_date in i and os.path.isfile(error_log_path + '/' + i):
                os.remove(error_log_path + '/' + i)
        # 删除普通的日志
        for i in os.listdir(normal_log_path):
            if i and (file_date in i) and os.path.isfile(normal_log_path + '/' + i):
                os.remove(normal_log_path + '/' + i)
        # 删除图片
        for i in os.listdir(picture_path):
            if i and (file_date in i) and os.path.isfile(picture_path + '/' + i):
                os.remove(picture_path + '/' + i)
    else:
        # 删除错误的日志
        for i in os.listdir(error_log_path):
            if os.path.isfile(error_log_path + '/' + i):
                os.remove(error_log_path + '/' + i)
        # 删除普通的日志
        for i in os.listdir(normal_log_path):
            if os.path.isfile(normal_log_path + '/' + i):
                os.remove(normal_log_path + '/' + i)
        # 删除图片
        for i in os.listdir(picture_path):
            if os.path.isfile(picture_path + '/' + i):
                os.remove(picture_path + '/' + i)


if __name__ == '__main__':
    delete_log_and_picture()
