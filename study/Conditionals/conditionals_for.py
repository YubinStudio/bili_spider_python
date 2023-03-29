#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : conditionals_for.py
# @Author: yubin
# @Date  : 2022/4/26
# @Desc  :

if __name__ == '__main__':
    for letter in 'Python':  # 第一个实例
        print("当前字母 : %s" % letter)

    print("-------------------------------------------------")
    fruits = ['banana', 'apple', 'mango']
    for fruit in fruits:  # 第二个实例
        print('当前水果 : %s' % fruit)

    print("-------------------------------------------------")
    for index in range(len(fruits)):
        print('当前水果 : %s' % fruits[index])

    print("-------------------------------------------------")
    i = 2
    while (i < 100):
        j = 2
        while (j <= (i / j)):
            if not (i % j): break
            j = j + 1
        if (j > i / j):
            print(i, " 是素数")
        i = i + 1
