import math
import os
from datetime import datetime
import requests
from bili_spider_process import get_mysql_connect
from writemysql import Write_2_Mysql
from writetext import TextStorage

"""
爬虫教程链接: https://blog.csdn.net/qq_44332894/article/details/109862654
"""


# B站番剧索引url连接在 浏览器控制台-》搜索api-》result-》preview返回番剧信息的请求url中
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36
# https://api.bilibili.com/pgc/season/index/result?season_version=-1&spoken_language_type=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&order=3&st=1&sort=0&page=1&season_type=1&pagesize=20&type=1
class MySpider(object):
    query_database = "test_db"
    query_table = "anime_info"
    idx = 1
    header = {
        "Referer": "https://www.bilibili.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    }

    def __init__(self, request_url, directory):
        self.s = requests.Session()
        self.url = request_url
        self.dir = directory
        if not os.path.exists(directory):
            os.mkdir(directory)
        # self.idx = 1

    def crawling(self):
        print("开始爬取……")
        s = requests.get(self.url, headers=MySpider.header)
        if s.status_code == 200:
            animelist = s.json()['data']['list']
            with TextStorage() as xs:
                for li in animelist:
                    anime_title = li['title']
                    anime_order = li['order']
                    anime_badge = li['badge']
                    anime_index = li['index_show']
                    anime_link = li['link']
                    image_url = li['cover']
                    filename = self.save_image(image_url)
                    content = anime_title + "\t" + anime_order + "\n" + anime_index + "\t" + anime_badge + \
                              "\n番剧链接：" + anime_link + "\n封面链接：" + image_url + \
                              "\n封面存放位置:" + self.dir + '/' + filename + "\n"
                    print(content)
                    xs.write(content)

    # 写入mysql - 使用with引用其他类方法 在__init__.py 中初始化表和清空表数据
    def crawling_4_mysql_with(self):
        print("开始爬取并写入MySQL……")
        s = requests.get(self.url, headers=MySpider.header)
        index = 0
        if s.status_code == 200:
            animelist = s.json()['data']['list']
            # 引用 Write_2_Mysql中的函数
            with Write_2_Mysql() as wm:
                for li in animelist:
                    anime_title = li['title']
                    anime_order = li['order']
                    anime_badge = li['badge']
                    anime_index = li['index_show']
                    anime_link = li['link']
                    image_url = li['cover']
                    update_time = datetime.now()
                    # 开始写入mysql
                    anime_data = [anime_title, anime_order, anime_badge, anime_index, anime_link, image_url,
                                  update_time]
                    wm.write_2_mysql(MySpider.query_database, MySpider.query_table, anime_data)
                    index += 1
                    print(str(index) + "--" + anime_title)

    # 写入mysql -(使用原生的方式)
    def crawling_4_mysql_origin(self):
        print("开始爬取并写入MySQL……")
        s = requests.get(self.url, headers=MySpider.header)
        index = 0
        if s.status_code == 200:
            animelist = s.json()['data']['list']
            # with Write_2_Mysql() as wm:
            conn = get_mysql_connect()
            cursor = conn.cursor()
            for li in animelist:
                anime_title = li['title']
                anime_order = li['order']
                anime_badge = li['badge']
                anime_index = li['index_show']
                anime_link = li['link']
                image_url = li['cover']
                update_time = datetime.now()
                # 开始写入mysql
                sql = "insert into anime_info(anime_title, anime_order, anime_badge, anime_index, anime_link, image_url,update_time) values (%s,%s,%s,%s,%s,%s,%s)"
                anime_data = [anime_title, anime_order, anime_badge, anime_index, anime_link, image_url,
                              update_time]

                cursor.execute(sql, anime_data)
                conn.commit()
                # anime_data.print_amime()
                # wm.write_2_mysql(anime_data)
                index += 1
                print(str(index) + "--" + anime_title)
            cursor.close()
            conn.close()

    def save_image(self, image_url):
        image = self.s.get(image_url, headers=MySpider.header)
        now = datetime.now()
        suffix = now.strftime('%Y%m%d_%H%M%S%f')
        name = "img_%s_%d.jpg" % (suffix, MySpider.idx)
        MySpider.idx += 1
        with open(self.dir + '/' + name, 'wb') as file:
            file.write(image.content)
        return name


if __name__ == "__main__":
    print("即将爬取追番人数从高到低的番剧信息。")
    global num
    # 每页最大值
    pagesize = 200

    while True:
        inp = None
        try:
            inp = int(input(
                "\t\033[1;034m请输入爬取数量页数,最大为%d页\n\t不输入或输入非整数默认为第1页 : " % (
                    math.ceil(3367 / pagesize))))
            print("\033[0m")
        except:
            pass
        if type(inp) == int:
            if inp > math.ceil(3367 / pagesize):
                print("\t\033[1;031m超出范围了！最大值为:", math.ceil(3367 / pagesize))
                continue
            num = inp
            break
        if inp == None:
            num = 1
            break

    for page in range(1, num + 1):
        url = "https://api.bilibili.com/pgc/season/index/result?season_version=-1&area=-1&is_finish=-1&copyright=-1" \
              "&season_status=-1&season_month=-1&year=-1&style_id=-1&order=3&st=1&sort=0" \
              "&page=%d&season_type=1&pagesize=%d&type=1" % (page, pagesize)

        print(url, " ==== num:", num)

        # 将数据写到文件中,图片写到picture文件夹
        # MySpider(url, "./picture").crawling()

        # 将数据写到MYSQL中，使用原生sql方式
        # MySpider(url, "./4mysql_org").crawling_4_mysql_origin()

        # 将数据写到MYSQL中，使用with关键字
        MySpider(url, "./4mysql_with").crawling_4_mysql_with()

    with Write_2_Mysql() as wm:
        wm.get_anime_count(MySpider.query_database, MySpider.query_table)
