#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : TestThread.py
# @Author: yubin
# @Date  : 2022/6/15
# @Desc  :

import time
import threading


def threadfunc(arg1, arg2):
    print("子线程开始\n")
    print(f"第一个参数是:{arg1},第二个参数是:{arg2}")
    print(threading.current_thread().name)
    time.sleep(3)
    print("子线程结束了")


thread1 = threading.Thread(target=threadfunc,name = 'thread1', args=(1, 2))
# thread2 = threading.Thread(target=threadfunc(args1=1, args2=2))
thread1.start()
# thread2.start()
for i in range(5):
    print(threading.current_thread().name+' main ', i)
    time.sleep(1)

print("主线程结束")
