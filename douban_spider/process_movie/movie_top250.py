#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : movie_top250.py
# @Author: yubin
# @Date  : 2022/4/28
# @Desc  :

from datetime import datetime
from queue import Queue
from threading import Thread, Lock
import pandas as pd
import requests
from lxml import etree
from sqlalchemy import create_engine


class MyDbMovieSpider(object):

    def __init__(self):
        self.df = []
        self.columns = ['排名', '电影名称(cn)', '电影名称(en)', '导演', '上映年份', '制作国家', '类型', '评分', '评价人数', '短评']
        self.lock = Lock()
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        }
        self.url_queue = Queue()

        # self.s = requests.Session()
        # self.url = url
        # self.directory = directory
        # if not os.path.exists(directory):
        #     os.mkdir(directory)

    def get_url(self):
        url = 'https://movie.douban.com/top250?start={}&filter='
        for i in range(0, 255, 25):
            self.url_queue.put(url.format(str(i)))
            print(url.format(str(i)))

    def get_html(self):
        while True:
            if not self.url_queue.empty():
                url = self.url_queue.get()
                resp = requests.get(url, headers=self.headers)
                html = resp.text
                self.xpath_parse(html)
            else:
                break

    def xpath_parse(self, html):
        xp = etree.HTML(html)
        movie_div = xp.xpath('//*[@id="content"]/div/div[1]/ol/li')
        # print("movie_div", movie_div)
        for li in movie_div:
            """排名、标题、导演、演员、"""
            ranks = li.xpath('div/div[1]/em/text()')
            titles_cn = li.xpath('div/div[2]/div[1]/a/span[1]/text()')[0].strip().replace('/', '').replace('\'',
                                                                                                           '').replace(
                '\"', '').replace(',', ' ')
            titles_en = li.xpath('div/div[2]/div[1]/a/span[2]/text()')[0].strip().replace('\xa0/\xa0', '').replace(
                '\xa0', '').replace('/', '').replace('\'', '').replace('\"', '').replace(',', ' ')
            directors = li.xpath('div/div[2]/div[2]/p[1]/text()')[0].strip().replace("\xa0\xa0\xa0", "\t").split(
                "\t")[0].replace('/', '').replace('\'', '').replace('\"', '')
            infos = li.xpath('div/div[2]/div[2]/p[1]/text()')[1].strip().replace('\xa0', '').split('/')
            date, areas, genres = infos[0], infos[1], infos[2]
            ratings = li.xpath('.//div[@class="star"]/span[2]/text()')[0]
            people = li.xpath('.//div[@class="star"]/span[4]/text()')[0][:-3]
            quotes = li.xpath('.//p[@class="quote"]/span/text()')

            # for rank, title, director in zip(ranks, titles_cn, directors):
            if len(quotes) == 0:
                quotes = None
            else:
                quotes = quotes[0]
            self.df.append(
                [str(ranks[0]), format(titles_cn), format(titles_en), format(directors), str(date), str(areas),
                 str(genres),
                 str(ratings), str(people), str(quotes)])

            res_frame = pd.DataFrame(self.df, columns=self.columns)

            res_frame.to_csv('./movies-top250/top_movies.csv', index=False)
            # res_frame.to_excel('./book-top250/top_movies.xlsx', index=False)

            # print(ranks, titles_cn, directors, date, areas, genres, ratings, scores, quotes)
            DB_STRING = 'mysql+mysqlconnector://root:123456@127.0.0.1/razer?charset=utf8'
            engine = create_engine(DB_STRING)
            # res_frame.to_sql('movies', engine, if_exists='append', index=False, chunksize=10000)

    def main(self):
        start_time = datetime.now()
        print("开始解析HTML...\t", start_time.strftime('%Y-%m-%d_%H:%M:%S'))
        self.get_url()

        th_list = []
        for i in range(5):
            th = Thread(target=self.get_html)
            th.start()
            th_list.append(th)

        for th in th_list:
            th.join()
        end_time = datetime.now()
        interval = end_time - start_time
        print("完成时间\t\t\t", end_time.strftime('%Y-%m-%d_%H:%M:%S'))
        print('消耗时间(s): ', interval)


if __name__ == '__main__':
    spider = MyDbMovieSpider()
    spider.main()

    # for start in range(0, 25, 25):
    #     url = "https://movie.douban.com/top250?start=%d" % start
    #     print(start, '---', url)
    #     MyDbMovieSpider(url, './book-top250').crawling()
