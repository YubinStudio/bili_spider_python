#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : book_top_250.py
# @Author: yubin
# @Date  : 2022/4/28
# @Desc  : 爬取豆瓣读书top-250

from datetime import datetime
from queue import Queue
from threading import Thread, Lock

import threading
import os
import shutil
import pandas as pd
import requests
from lxml import etree
from sqlalchemy import create_engine


class MyDbBookSpider():

    def __init__(self, directory):
        self.session = requests.Session()
        self._index = 1
        self.img_index = 1
        self.df = []

        # self.columns = ['序号', '书名', '作家信息', '评分', '评分人数', '简述', '图片链接']
        self.columns = ['序号', '书名', '作家', '译者', '出版社', '初版时间', '定价', '评分', '评分人数', '简述', '图片链接']
        self.lock = Lock()
        self.url_queue = Queue()
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        }

        self.dir = directory
        # 要清空的文件夹名
        shutil.rmtree(directory)
        if not os.path.exists(directory):
            os.mkdir(directory)

    def get_url(self):
        url = 'https://book.douban.com/top250?start={}&filter='
        for i in range(0, 350, 25):
            self.url_queue.put(url.format(str(i)))

    def get_html(self):
        while True:
            if not self.url_queue.empty():
                url = self.url_queue.get()
                resp = requests.get(url, headers=self.headers)
                html = resp.text
                self.xpath_parse(html)
                print('当前线程名 : ',threading.current_thread().name)
            else:
                break

    def save_image(self, image_url):
        image = self.session.get(image_url, headers=self.headers)
        now = datetime.now()
        suffix = now.strftime('%Y%m%d_%H%M')
        name = "img_%s_%d.jpg" % (suffix, self.img_index)
        self.img_index += 1
        with open(self.dir + '/' + name, 'wb') as file:
            file.write(image.content)
        return name

    def xpath_parse(self, html):
        xp = etree.HTML(html)
        book_div = xp.xpath('//*[@id="content"]/div/div[1]/div/table')
        # print("book_div", book_div)
        author = ''
        translator = ''
        publishing_house = ''
        first_edition_time = ''
        price = ''

        for book in book_div:
            # './/p[@class="quote"]'
            book_name = book.xpath('tr/td[2]/div[1]/a/text()')[0].strip().replace(' ', '')
            info = book.xpath('tr/td[2]/p/text()')[0]
            score = book.xpath('tr/td[2]/div[2]/span[2]/text()')[0].strip()
            people = book.xpath('tr/td[2]/div[2]/span[3]/text()')[0].strip().replace(' ', '').replace('(', '').replace(
                ')', '').replace('\n', '').strip()[:-3]
            desc = book.xpath('.//p[@class="quote"]/span/text()')  # [0]
            image_url = book.xpath('tr/td[1]/a/img/@src')[0].strip()
            # 保存图片
            self.save_image(image_url)
            #
            info_spt = info.split('/')
            # ['序号', '书名', '作家' ,'译者', '出版社' ,'初版时间', '定价', '评分', '评分人数', '简述', '图片链接']

            if len(desc) == 0:
                desc = None
            else:
                desc = desc[0].strip().replace(' ', '')

            if len(info_spt) == 4:
                author = info_spt[0].strip()
                translator = ''
                publishing_house = info_spt[1].strip()
                first_edition_time = info_spt[2].strip()
                price = info_spt[3].strip()
            elif len(info_spt) == 5:
                author = info_spt[0].strip()
                translator = info_spt[1].strip()
                publishing_house = info_spt[2].strip()
                first_edition_time = info_spt[3].strip()
                price = info_spt[4].strip()

            # self.df.append([self._index, str(book_name), str(info), str(score), str(people), str(desc), str(image_url)])
            self.df.append([self._index, str(book_name), str(author), str(translator), str(publishing_house),
                            str(first_edition_time), str(price), str(score), str(people), str(desc),
                            str(image_url)])
            self._index += 1

            print(self._index, threading.current_thread().name, str(book_name), str(author), str(translator),
                  str(publishing_house),
                  str(first_edition_time), str(price), str(score), str(people), str(desc),
                  str(image_url))

            # self.df.append([head, info, score, people, desc ,image_url])
            res_frame = pd.DataFrame(self.df, columns=self.columns)
            # 写入csv文件
            res_frame.to_csv('./book-top250/top_books.csv', index=False)
            # res_frame.to_excel('./book-top250/top_books.xlsx', index=False)

            # 写入MySQL
            DB_STRING = 'mysql+mysqlconnector://root:123456@127.0.0.1/razer?charset=utf8'
            engine = create_engine(DB_STRING)
            res_frame.to_sql('books', engine, if_exists='replace', index=False, chunksize=10000)

    def main(self):
        start_time = datetime.now()
        print("开始解析HTML...\t", start_time.strftime('%Y-%m-%d %H:%M:%S'))
        # 调用get_url方法获取url
        self.get_url()

        thread_list = []
        for i in range(5):
            # thead = Thread(target=self.get_html, name='childThread')
            thead = Thread(target=self.get_html(), name='childThread')
            thead.start()
            thread_list.append(thead)

        for th in thread_list:
            th.join()

        end_time = datetime.now()
        interval = end_time - start_time
        print("完成时间\t\t\t", end_time.strftime('%Y-%m-%d %H:%M:%S'))
        print('消耗时间(s): ', interval)


if __name__ == '__main__':
    spider = MyDbBookSpider('./picture')
    spider.main()
