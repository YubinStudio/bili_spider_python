#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : TestSplit.py
# @Author: yubin
# @Date  : 2022/6/15
# @Desc  :

if __name__ == '__main__':
    cn_str = '陈凯歌 / 人民文学出版社 / 2001-6 / 10.00元'
    en_str = '[意] 卡洛·罗韦利 / 杨光 / 湖南科学技术出版社 / 2019-6 / 56.00元'
    cn_result = cn_str.split('/')
    en_result = en_str.split('/')

    print(cn_result)
    print(cn_result[1].strip())
    print(len(cn_result))

    print('--------------------------------')
    print(en_result)
    print(en_result[1].strip())
    print(len(en_result))

    print('---------------------------------')
    temp = '[英] 莎士比亚 / 朱生豪 / 人民文学出版社 / 2001-1 / 7.00元'
    if temp.__contains__('[') and temp.__contains__(']'):
        print('1111111')
    else:
        print('2222222')

    print(temp.strip().split(']')[0].startswith('['))