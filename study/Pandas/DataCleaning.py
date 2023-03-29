#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : DataCleaning.py
# @Author: yubin
# @Date  : 2022/7/20
# @Desc  :
# Pandas 数据清洗
#   数据清洗是对一些没有用的数据进行处理的过程。
#   很多数据集存在数据缺失、数据格式错误、错误数据或重复数据的情况，如果要对使数据分析更加准确，就需要对这些没有用的数据进行处理。
#   在这个教程中，我们将利用 Pandas包来进行数据清洗

import pandas as pd

# TODO 1 读取csv文件,isnull()判断是否空值，Pandas 把 n/a 和 NA 当作空数据，na 不是空数据，不符合我们要求，我们可以指定空数据类型：
csv = pd.read_csv('property-data.csv')
# print(csv['NUM_BEDROOMS'])
# print(csv['NUM_BEDROOMS'].isnull())

# 如果我们要删除包含空字段的行，可以使用 dropna() 方法，语法格式如下：
#   DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
#       参数说明：
#           axis：默认为 0，表示逢空值剔除整行，如果设置参数 axis＝1 表示逢空值去掉整列。
#           how：默认为 'any' 如果一行（或一列）里任何一个数据有出现 NA 就去掉整行，如果设置 how='all' 一行（或列）都是 NA 才去掉这整行。
#           thresh：设置需要多少非空值的数据才可以保留下来的。
#           subset：设置想要检查的列。如果是多个列，可以使用列名的 list 作为参数。
#           inplace：如果设置 True，将计算得到的值直接覆盖之前的值并返回 None，修改的是源数据。
#           我们可以通过 isnull() 判断各个单元格是否为空。
# 注意：默认情况下，dropna() 方法返回一个新的 DataFrame，不会修改源数据。
# 如果你要修改源数据 DataFrame, 可以使用 inplace = True 参数:

# TODO 2 missing_values 过滤数据
missing_values = []
# missing_values = ["n/a", "na", "--"]
miss_df = pd.read_csv('property-data.csv', na_values=missing_values)
# print(miss_df)
# print(miss_df['NUM_BEDROOMS'])
# print(miss_df['NUM_BEDROOMS'].isnull())
print('--------------------------------')
# TODO 3 使用dropna() 过滤 ST_NUM列为空值的行
del_df = miss_df.dropna(subset=['ST_NUM'])
# print(del_df)

# TODO 4 我们也可以 fillna() 方法来替换一些空字段：
fill_df = pd.read_csv('property-data-1.csv')
# fill_df.fillna(12345)
# fill_df.fillna(12345, inplace=True)
# print(fill_df.to_string())
print('--------------------------------')
fill_df['PID'].fillna(11111, inplace=True)
# print(fill_df.to_string())

# TODO 5 使用 mean() 方法计算列的均值并替换空单元格：
mean_df = pd.read_csv('property-data-1.csv')
# mean()计算平均值,使用median()方法计算列的中位数,使用mode()方法计算列的众数（出现频率最高的数）
x = mean_df['ST_NUM'].mean()
y = mean_df['ST_NUM'].median()
z = mean_df['ST_NUM'].mode()
# print('平均值 : ', x,' 中位数 : ', y,' 众数 : ', z)

mean_df['ST_NUM'].fillna(x, inplace=True)
# print(mean_df.to_string())


# TODO 6 Pandas 清洗错误数据
person = {
    "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
    "age": [50, 40, 40, 12345]  # 12345 年龄数据是错误的
}

person_df = pd.DataFrame(person)
# TODO 6.1 使用位置替换数据
# person_df.loc[2, 'age'] = 18  # 修改数据
# print(person_df.to_string())

# TODO 6.2 设置条件语句替换数据
# for x in person_df.index:
#     if person_df.loc[x, 'age'] > 120:
#         person_df.loc[x, 'age'] = 120
# print(person_df.to_string())
# TODO 6.3 设置条件语句删除数据
# for x in person_df.index:
#     if person_df.loc[x, 'age'] > 120:
#         person_df.drop(x, inplace=True)
# print(person_df.to_string())
# TODO 6.4 Pandas 清洗重复数据
#   如果我们要清洗重复数据，可以使用 duplicated() 和 drop_duplicates() 方法。
#   如果对应的数据是重复的，duplicated() 会返回 True，否则返回 False。
print(person_df, '\n')
print(person_df.duplicated())

#   删除重复数据，可以直接使用drop_duplicates() 方法。
person_df.drop_duplicates(inplace=True)
print('\n', person_df)
