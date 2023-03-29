#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : __init__.py.py
# @Author: yubin
# @Date  : 2021/11/11
# @Desc  :
import pymysql

from writemysql import Write_2_Mysql

_host = "localhost"
_user = "root"
_password = "123456"
_database = "test_db"
_table = "anime_info"
_charset = "utf8"

# 初始化表和清空表数据
with Write_2_Mysql() as wm:
    wm.database_exists(_database)
    wm.table_exists(_table)
    wm.truncate_anime_tab(_database, _table)


def get_mysql_connect():
    conn = pymysql.connect(host=_host, user=_user, password=_password, database=_database, charset=_charset)
    return conn
    # 判断表是否存在
