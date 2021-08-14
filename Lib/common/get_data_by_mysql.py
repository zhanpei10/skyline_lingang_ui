'''
从数据库查询数据进行断言
'''
from Lib.common.common_function import get_mysql_config
import pymysql


class MysqlAssert:

    def __init__(self):
        self.conn = pymysql.connect(**get_mysql_config('SIT_MYSQL'))

    def get_count(self, table, column_dic):
        '''
        获取数据的条数
        :return:
        '''
        for key, value in column_dic.items():
            pass
        c = self.conn.cursor(pymysql.cursors.DictCursor)
        count = c.execute(sql)
        return count
