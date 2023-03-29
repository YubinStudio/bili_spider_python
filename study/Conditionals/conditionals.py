#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : conditionals.py
# @Author: yubin
# @Date  : 2022/4/26
# @Desc  :

if __name__ == '__main__':
    while True:
        num = int(input("输入一个数 : "))
        if num % 2 == 0:
            print(num, " 是偶数")
        else:
            print(num, " 是奇数")
