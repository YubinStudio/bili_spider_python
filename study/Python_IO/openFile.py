#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : openFile.py
# @Author: yubin
# @Date  : 2022/4/27
# @Desc  :

"""
文件使用方式open（）函数的参数说明
    'r':默认值，表示从文件读取数据。
    'w':表示要向文件写入数据，并截断以前的内容
    'a':表示要向文件写入数据，添加到当前内容尾部
    'r+':表示对文件进行可读写操作（删除以前的所有数据）
    'r+a'：表示对文件可进行读写操作（添加到当前文件尾部）
    'b':表示要读写二进制数据
"""
if __name__ == '__main__':
    path = "../file_test.txt"
    # file = open(path, encoding='gbk', errors='ignore')
    file = open(path, 'r+', encoding='utf-8')

    print(file.name)

    # for num in range(1, 10):
    #     file.write(str(num) + "\n")

    # print(file.read())
    # for line in file:
    #     print(line)

    print("----------------------------")
    cnt = 0
    for line in file:
        # print("line.find('when'): ",line.find('when') )
        print(line.startswith('when'))
        if line.find('when') == 0:
            cnt += 1

    print("cnt: ", cnt)

    file.close()
