#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : DataFrame.py
# @Author: yubin
# @Date  : 2022/7/19
# @Desc  : Pandas 数据结构 - DataFrame
#   DataFrame 是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔型值）。DataFrame 既有行索引也有列索引，它可以被看做由 Series 组成的字典（共同用一个索引）
# DataFrame 构造方法如下：
#     pandas.DataFrame( data, index, columns, dtype, copy)
# 参数说明：
#     data：一组数据(ndarray、series, map, lists, dict 等类型)。
#     index：索引值，或者可以称为行标签。
#     columns：列标签，默认为 RangeIndex (0, 1, 2, …, n) 。
#     dtype：数据类型。
#     copy：拷贝数据，默认为 False。

import pandas as pd

# 实例 - 使用列表创建
data = [['Google', 10], ['Run', 12], ['Wiki', 13]]
df = pd.DataFrame(data, columns=['site', 'rank'], dtype=float)
print(df)
print('-----------------------')
# 实例 - 使用 ndarrays 创建
data_n = {'site': ['Google', 'Runoob', 'Wiki'], 'rank': [10, 12, 13]}
_data = pd.DataFrame(data_n)
print(_data)
