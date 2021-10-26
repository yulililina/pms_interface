#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# creater:yulili

"""
1.配置环境信息
"""

import os
# 当前脚本所在目录的上级目录
src_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# 62环境地址信息配置
# swagger地址信息配置
s_host = '192.168.161.62'
s_port = 9100

# 数据库地址信息
host_test = '192.168.161.18'
user_test = 'db_admin'
password_test = 'light2902'
name_test = 'lingxiao_pms'
port_test = 3306


request_url = 'http://{}:{}'.format(s_host,s_port)

