#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : operator.py
# @Author: yubin
# @Date  : 2022/4/26
# @Desc  :

if __name__ == '__main__':
    a = 21
    b = 10
    c = 0

    c = a + b
    print("1 - c 的值为：", c)


    c = a - b
    print("2 - c 的值为：", c)

    c = a * b
    print("3 - c 的值为：", c)


    c = a / b
    print("4 - c 的值为：", c)


    c = a % b
    print("5 - c 的值为：", c)


    # 修改变量 a 、b 、c
    a = 2
    b = 3
    c = a ** b
    print("6 - c 的值为：", c)

    #取整除 - 返回商的整数部分（向下取整）
    a = 10
    b = 6
    c = a // b
    print("7 - c 的值为：", c)
