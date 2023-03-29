#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : exception_demo.py
# @Author: yubin
# @Date  : 2021/11/5
# @Desc  :
"""
try-except
"""
# try:
#     fh = open("test.txt", "a+", encoding='utf-8')
#     fh.write("这是一个测试文件，用于测试异常!!\n")
#     raise IOError()  # 手动触发异常
# except IOError:
#     print("Error: 没有找到文件或读取文件失败")
# else:
#     print("内容写入文件成功")
#     fh.close()

"""
try-finally-except
"""
# try:
#     fh = open("test.txt", "w", encoding='utf-8')
#     try:
#         fh.write("这是一个测试文件，用于测试异常!!\n")
#         raise IOError()  # 手动触发异常
#     finally:
#         print("关闭文件流")
#         fh.close()
# except IOError:
#     print("Error: 没有找到文件或读取文件失败")
# else:
#     print("内容写入文件成功")
#     fh.close()


"""
try-finally-except 捕获多个异常
"""
try:
    fh = open("test.txt", "w", encoding='utf-8')
    try:
        fh.write("这是一个测试文件，用于测试异常!!\n")
        raise IOError()  # 手动触发异常
        # raise AttributeError("_input_parm")
        # raise TypeError(int)
    finally:
        print("关闭文件流")
        fh.close()
except IOError:
    print("Error: 没有找到文件或读取文件失败")
except AttributeError as args:
    print("except_参数错误", args)
except TypeError as type_args:
    print("except_类型错误", type_args)
else:
    print("内容写入文件成功")
    fh.close()