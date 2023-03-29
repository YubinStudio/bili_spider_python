#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : get_holidays.py
# @Author: yubin
# @Date  : 2022/4/26
# @Desc  :

import datetime
import chinese_calendar
import numpy

class DayUtils(object):

    def get_holidays(year=None, include_weekends=True):
        """
        获取某一年的所有节假日，默认当年
        :param year: which year
        :param include_weekends: False for excluding Saturdays and Sundays
        :return: list
        """
        if not year:
            year = datetime.datetime.now().year
        else:
            year = year
        start = datetime.date(year, 1, 1)
        end = datetime.date(year, 12, 31)
        holidays = chinese_calendar.get_holidays(start, end, include_weekends)
        return holidays

    def get_workdays(year=None):
        """
        获取某一年的所有工作日，默认当年
        :param year: which year
        :param include_weekends: False for excluding Saturdays and Sundays
        :return: list
        """
        if not year:
            year = datetime.datetime.now().year
        else:
            year = year
        start = datetime.date(year, 1, 1)
        end = datetime.date(year, 12, 31)
        workdays = chinese_calendar.get_workdays(start, end)
        return workdays
    def list2array(self,list):
        """
        将list转化为numpy
        :param list:
        :return:
        """
        return numpy.array(list)

if __name__ == '__main__':
    print("获取节假日包含周末  -- 数据类型 --",type(DayUtils.get_holidays(2022)))
    print(DayUtils.get_holidays(2022))
    print("获取工作日         -- 数据类型 --",type(DayUtils.get_workdays(2022)))
    print(DayUtils.get_workdays(2022))

    # 获取日期-剔除周末
    holidays = DayUtils.get_holidays(2022, 0)
    # print(holidays)

    #定义一个新list
    str_holidays = []
    print("获取节假日不包含周末  -- 数据类型 --",type(str_holidays))
    for day in holidays:
        str_holidays.append(day.strftime("%Y-%m-%d"))

    print(str_holidays)
