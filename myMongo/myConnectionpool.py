"""
Author: SoChichung
Date: 2022-07-21 21:30:34
LastEditors: SoChichung
LastEditTime: 2022-07-28 06:30:00
Description: 

Copyright (c) 2022 by SoChichung ddeadwings@gmail.com, All Rights Reserved. 
"""
"""
Author: SoChichung
Date: 2022-07-21 21:30:34
LastEditors: SoChichung
LastEditTime: 2022-07-28 05:56:43
Description: 

Copyright (c) 2022 by SoChichung ddeadwings@gmail.com, All Rights Reserved. 
"""
"""
Author: SoChichung
Date: 2022-07-21 21:30:34
LastEditors: SoChichung
LastEditTime: 2022-07-23 10:36:26
Description:

Copyright (c) 2022 by SoChichung ddeadwings@gmail.com, All Rights Reserved. 
"""
# -*- encoding: utf-8 -*-


import pymongo
import mongo_config as config
import time

# 单例模式函数，用来修饰类


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


class MyConnectionPool:
    # 私有属性
    # 能通过对象直接访问，但是可以在本类内部访问；
    _pool = None
    # def __init__(self):
    #     self.conn = self.__getConn()
    #     self.cursor = self.conn.cursor()
    def __enter__(self):
        self.conn = self.__getconn()

    def __getconn(self):
        # i = random.randint(1, 100)
        # print("创建线程池的数量"+str(i))
        if self._pool:
            return self._pool
        else:
            mongo_url = "mongodb://{0}:{1}@{2}:{3}/".format(
                config.DB_TEST_USER,
                config.DB_TEST_PASSWORD,
                config.DB_TEST_HOST,
                config.DB_TEST_PORT,
            )
            self._pool = pymongo.MongoClient(mongo_url)
            # 用时间戳作为他的指针
            # self._pool.cursor = time.time()
        return self._pool

    # 从连接池中取出一个连接
    def getconn(self):
        conn = self.__getconn()
        # cursor = conn.cursor
        return conn


# 获取连接池,实例化
@singleton
def get_my_connection():
    return MyConnectionPool()
