# -*- encoding: utf-8 -*-

"""
Author: SoChichung
Date: 2022-07-21 21:30:34
LastEditors: SoChichung
LastEditTime: 2022-07-23 10:00:26
Description: 连接池文件

Copyright (c) 2022 by SoChichung ddeadwings@gmail.com, All Rights Reserved. 
"""


import pymongo
import mongo_config as config

# 单例模式函数，用来修饰类

def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


class myConnectionPool():
    # 私有属性
    # 能通过对象直接访问，但是可以在本类内部访问；
    _pool=None
    def __enter__(self):
        self.conn = self.__getconn()
    def __getconn(self):
        if self._pool is None:
            mongo_url = "mongodb://{0}:{1}@{2}:{3}/".format
            (config.username, config.passwd, config.host, config.port)
            


