#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : conditionals_continue.py
# @Author: yubin
# @Date  : 2022/4/26
# @Desc  :
"""
Python continue 语句跳出本次循环，而break跳出整个循环。
continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
continue语句用在while和for循环中。
"""

if __name__ == '__main__':
    for letter in 'Python':  # 第一个实例
        if letter == 'h':
            continue
        print('当前字母 :', letter)

    var = 10  # 第二个实例
    while var > 0:
        var = var - 1
        if var == 5:
            continue
        print('当前变量值 :', var)
