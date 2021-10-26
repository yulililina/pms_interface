#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# creater:yulili

"""自定义封装logger"""

import logging, sys
from public import config

# 日志封装为类
# class Deflogger(object):
#
#     def __init__(self):
#         # 获取 Deflogger 实例
#         logger = logging.getLogger("")
#
#         # 指定log输出日志
#         format_log = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
#
#         # 输出文件日志
#         file_handler = logging.FileHandler(config.src_path + '/log/interface_test.log')
#         file_handler.setFormatter(format_log)
#
#         # 控制台日志
#         console_handler = logging.StreamHandler(sys.stdout)
#         console_handler.setFormatter(format_log)
#
#         # 为logger添加具体的日志处理器
#
#         logger.addHandler(file_handler)
#         logger.addHandler(console_handler)
#
#         logger.setLevel(logging.DEBUG)
#         self.logger = logger
#
#
# if __name__ == '__main__':
#     test = Deflogger()
#     logger = test.logger
#     logger.info("u209fiojijfi")

# 日志封装为方法
def logger_test():
    # 获取 logger 实例
    logger = logging.getLogger("")

    # 指定log输出日志
    format_log = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

    # 输出文件日志
    file_handler = logging.FileHandler(config.src_path + '/log/interface_test.log')
    file_handler.setFormatter(format_log)

    # 控制台日志
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(format_log)

    # 为logger添加具体的日志处理器

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.setLevel(logging.DEBUG)
    return logger


if __name__ == '__main__':
    logger = logger_test()
    logger.info("这是一个错误日志")









