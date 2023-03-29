#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Series.py
# @Author: yubin
# @Date  : 2022/7/19
# @Desc  :
#       Pandas Series 类似表格中的一个列（column），类似于一维数组，可以保存任何数据类型。
#       Series 由索引（index）和列组成，函数如下：
#       pandas.Series( data, index, dtype, name, copy)
# 参数说明：
#         data：一组数据(ndarray 类型)。
#         index：数据索引标签，如果不指定，默认从 0 开始。
#         dtype：数据类型，默认会自己判断。
#         name：设置名称。
#         copy：拷贝数据，默认为 False。

import pandas as pd

# 不指定索引，使用默认索引
a = [1, 2, 3]
arr = pd.Series(a)
print(arr)
print("arr[1] : ", arr[1])
print('---------------------')
print('---------------------')
# 指定自定义索引
b = ['hello', 'pandas', 'series']
ind_arr = pd.Series(b, index=['x', 'y', 'z'])
print(ind_arr)
print('索引x的值 : ', ind_arr['x'])
print('---------------------')
print('---------------------')
# 使用 key/value 对象，类似字典来创建 Series
data = {'a': 'hello', 'b': 'pandas', 'c': 'series'}
dic_arr = pd.Series(data)
print(dic_arr)
print('索引b的值 : ', dic_arr['b'])
