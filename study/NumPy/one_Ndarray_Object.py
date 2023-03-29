#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : one_Ndarray_Object.py
# @Author: yubin
# @Date  : 2022/7/20
# @Desc  :  TODO 链接 https://www.runoob.com/numpy/numpy-ndarray-object.html
# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
#       参数说明：
#           object	数组或嵌套的数列
#           dtype	数组元素的数据类型，可选
#           copy	对象是否需要复制，可选
#           order	创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
#           subok	默认返回一个与基类类型一致的数组
#           ndmin	指定生成数组的最小维度
import numpy as np

a = np.array([1, 2, 3])
print(a)
print('--------------')
b = np.array([[1, 2], [3, 4]])
print(b)
print('--------------')
c = np.array([[1, 2], [3, 4]], ndmin=1)
print(c)
print('--------------')
d = np.array([1, 2, 3], dtype=complex)
print(d)
