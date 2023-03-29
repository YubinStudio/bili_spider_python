#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : ComparisonOperators.py
# @Author: yubin
# @Date  : 2022/4/26
# @Desc  :


if __name__ == '__main__':

    a = 21
    b = 10
    c = 0

    if a == b:
        print("1 - a 等于 b")
    else:
        print("1 - a 不等于 b")

    if a != b:
        print("2 - a 不等于 b")
    else:
        print("2 - a 等于 b")

    # python3 已废弃。
    # if a <> b:
    #     print
    #     "3 - a 不等于 b"
    # else:
    #     print
    #     "3 - a 等于 b"

    if a < b:
        print("4 - a 小于 b")
    else:
        print("4 - a 大于等于 b")

    if a > b:
        print("5 - a 大于 b")
    else:
        print("5 - a 小于等于 b")

    # 修改变量 a 和 b 的值
    a = 5
    b = 20
    if a <= b:
        print("6 - a 小于等于 b")
    else:
        print("6 - a 大于  b")

    if b >= a:
        print("7 - b 大于等于 a")
    else:
        print("7 - b 小于 a")
