#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : List.py
# @Author: yubin
# @Date  : 2022/4/26
# @Desc  :

if __name__ == '__main__':
    list = []
    list.append("python")
    list.append("quick")
    list.append("start")

    print(list)
    # 删除元素
    del list[2]
    print(list)

    for index in range(len(list)):
        print("第%s元素是%s" % (index, list[index]))

    for index, elem in enumerate(list):
        print("第%s元素是%s" % (index, elem))
