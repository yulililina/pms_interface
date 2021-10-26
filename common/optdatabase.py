#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# creater:yulili

"""
定义对mysql数据库基本操作的封装
1.包括基本的单条语句操作，删除、自改、更新
"""
import os,logging,pymysql
from public import config
from common import deflogger

HOST = config.host_test
PORT = config.port_test
USERNAME = config.user_test
PASSWORD = config.password_test
DBNAME = config.name_test


class OperationDbInterface(object):

    # 初始化数据库连接
    def __init__(self,host_db=HOST,user_db=USERNAME,passwd_db=PASSWORD,name_db=DBNAME,port_db=PORT,link_type=0):
        """
        :param host_db: 数据库服务主机
        :param user_db: 数据库用户名
        :param passwd_db: 数据库密码
        :param name_db: 数据库名称
        :param port_db: 端口晚上号，整型数字
        :param link_type: 链接类型，用于输出数据是元祖还是字典，默认是字典，link_type=0
        :return:游标
        """
        try:
            if link_type == 0:
                # 创建数据库链接,返回字典
                self.conn = pymysql.connect(host=host_db,user=user_db,passwd=passwd_db,db=name_db,
                                            port=port_db,charset='utf8',cursorclass=pymysql.cursors.DictCursor)
            else:
                # 创建数据库连接，返回元祖
                self.conn = pymysql.connect(host=host_db,user=user_db,passwd=passwd_db,db=name_db,
                                            port=port_db,charset='utf8')
            self.cur = self.conn.cursor()
        except pymysql.Error as error:
            print("创建数据库连接失败|Mysql Error %d:%s" % (error.args[0],error.args[1]))
            logger = deflogger.logger_test()
            logger.exception(error)







if __name__ == "__main__":
    test = OperationDbInterface() # 初始化数据库连接














