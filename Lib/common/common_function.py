# 添加常用的公共函数
import configparser
import os


# 获取项目的根路径
def get_path():
    return os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


# 读取配置文件信息，获得环境地址
def get_url(environment, key):
    conf = configparser.ConfigParser()
    conf.read(get_path() + '/Config/environment.ini')
    return conf.get(environment.upper(), key)


if __name__ == '__main__':
    print(get_path())
    print(get_url('sit', 'sit_lg'))
