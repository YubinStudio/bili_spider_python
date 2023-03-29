import pymysql

"""
# 1.使用with语句的目的就是把代码块放入with中执行，with结束后，自动完成清理工作，无须手动干预
# 2.在需要管理一些资源比如文件，网络连接和锁的编程环境中，可以在__exit__中定制自动释放资源的机制，你无须再去关系这个问题，这将大有用处

前双下划线(__age):表示私有类型的变量(privated)，只能在本类中进行访问，外界不能直接访问。如__age.
单下划线(_age)：以单下划线开头的表示保护类型变量(protected)，
保护类型的变量只允许本身以及子类访问，不能用于from module import *
[使用单下划线开头的时候，虽然变量能够直接被访问，但是请把变量视为一个保护类型的变量，尽量不要去访问
"""


class Write_2_Mysql(object):
    # 类变量-使用类名. 调用
    __host = "localhost"
    __user = "root"
    __password = "123456"
    __database = "test_db"
    __charset = "utf8"

    def __init__(self):
        """

        """
        self.enter_flag = 0
        conn = pymysql.connect(
            host=Write_2_Mysql.__host,
            user=Write_2_Mysql.__user,
            password=Write_2_Mysql.__password,
            database=Write_2_Mysql.__database,
            charset=Write_2_Mysql.__charset
        )
        self.conn = conn
        self.cursor = conn.cursor()

    def __enter__(self):
        """
        对象的__enter__被触发, 有返回值则赋值给as声明的变量
        :return:
        """
        # 成员变量
        self.enter_flag = 1
        return self

    def __exit__(self, Type, value, traceback):
        """
        with语句中代码块出现异常，则with后的代码都无法执行
        :param Type: 异常类型
        :param value: 异常值
        :param traceback: 追溯信息
        """
        if self.enter_flag:
            print("MySQL连接 : ", self.conn, " __flag = ", self.enter_flag)
            # 关闭光标对象
            self.cursor.close()
            # 关闭数据库连接
            self.conn.close()
            print("已关闭MySQL连接！！！")

    def write_2_mysql(self, anime_data):
        """
        调用函数将数据插入到MySQL
        :param anime_data:
        """
        try:
            sql = "insert into anime_info(anime_title, anime_order, anime_badge, anime_index, anime_link, image_url,update_time) values (%s,%s,%s,%s,%s,%s,%s)"
            try:
                "数据写入MySQL"
                self.cursor.execute(sql, anime_data)
                self.conn.commit()
            finally:
                pass
                # print("finally!！")
                # self.cursor.close()
                # self.conn.close()
        except (AttributeError) as args:
            print("输入参数错误！", args)
        except (IOError) as args:
            print("IO错误！", args)

    def truncate_anime_tab(self):
        """
        调用函数清空表
        """
        truncate_sql = "truncate table anime_info"
        self.cursor.execute(truncate_sql)

    def get_anime_list(self):
        empty_flag = 0
        try:
            sql = "select count(1) from anime_info"
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            if result[0] > 0:
                empty_flag = 1
        except (AttributeError) as args:
            print("输入参数错误！", args)
        except IOError as args:
            print("IO错误！", args)
        print("empty_flag",empty_flag)
        return empty_flag
