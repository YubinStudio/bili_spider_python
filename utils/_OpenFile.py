#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : _OpenFile.py
# @Author: yubin
# @Date  : 2021/11/5
# @Desc  :
class Open:
    name = "class-param"
    def __init__(self,name):
        self.name=name

    def __enter__(self):
        print('出现with语句,对象的__enter__被触发,有返回值则赋值给as声明的变量')
        # self.name = '__enter__method'
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('with中代码块执行完毕___exit__')


with Open('a.txt') as f:
    print('=====>执行代码块 ==>',f.name)
    # print(f,f.name)
    raise AttributeError('嘿嘿')
    print("Open内")
print("外")