#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : app_spider.py
# @Author: yubin
# @Date  : 2022/4/27
# @Desc  :
import datetime
import requests


class JD_Spider(object):
    header = {
        "Referer": "",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    }

    url_jd = "https://item.jd.com/100029206596.html"
    # url_jd = "https://club.jd.com/comment/productCommentSummaries.action?referenceIds=100029206596&callback=jQuery679716&_=1651030424646"
    # url_jd = "https://search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BA%E6%89%8B%E8%A1%A8&enc=utf-8&pvid=6314018f14b64c178ca4b934263a5768"

    def crawling(self):
        print("开始爬取……")
        result_req = requests.get(self.url_jd, self.header)
        # if result_req.status_code == 200:
        #     result = result_req.json()['m-list']
        #     print(result)

        print(result_req.content)


if __name__ == '__main__':
    JD_Spider().crawling()
