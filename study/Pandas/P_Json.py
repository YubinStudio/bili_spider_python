#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : P_Json.py
# @Author: yubin
# @Date  : 2022/7/19
# @Desc  :

import pandas as pd

student_info = {
    "school_name": "ABC primary school",
    "class": "Year 1",
    "students": [
        {
            "id": "A001",
            "name": "Tom",
            "math": 60,
            "physics": 66,
            "chemistry": 61
        },
        {
            "id": "A002",
            "name": "James",
            "math": 89,
            "physics": 76,
            "chemistry": 51
        },
        {
            "id": "A003",
            "name": "Jenny",
            "math": 79,
            "physics": 90,
            "chemistry": 78
        }]
}

site_info = [
    {
        "id": "A001",
        "name": "菜鸟教程",
        "url": "www.runoob.com",
        "likes": 61
    },
    {
        "id": "A002",
        "name": "Google",
        "url": "www.google.com",
        "likes": 124
    },
    {
        "id": "A003",
        "name": "淘宝",
        "url": "www.taobao.com",
        "likes": 45
    }
]

# read_json()读取.json文件
# p_json = pd.read_json(json_data_1)

# student = pd.DataFrame(student_info)
# 使用json_normalize()展平数据,获取对应key的value
student = pd.json_normalize(student_info, record_path='students', meta=['school_name', 'class'])
print(student)
print(type(student))
print('--------------------------')
site = pd.json_normalize(site_info)
print(site)
