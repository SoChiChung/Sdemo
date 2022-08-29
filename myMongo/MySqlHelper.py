"""
Author: SoChichung
Date: 2022-07-23 17:08:52
LastEditors: SoChichung
LastEditTime: 2022-08-29 06:58:11
Description: 

Copyright (c) 2022 by SoChichung ddeadwings@gmail.com, All Rights Reserved. 
"""
import time
import Myconnection

# print(dir(Myconnection))
class SqlHelper:
    def __init__(self, dbname):
        connection = Myconnection.Myconnection()
        self.client = connection.getClient()
        client = self.client
        self.db = client[dbname]

    # 执行命令
    # 增
    def insert_one(self,collection, item):
        db = self.db
        dbcollection = db[collection]
        try:
            if dbcollection.findone(item):
                print("对象已存在，无法写入！")
            else:
                dbcollection.insert_one(item)
                print("插入成功！")
        except Exception as e:
            print("报错：" + e.__str__())

    def insert_many(self,collection, item_list):
        db = self.db
        dbcollection = db[collection]
        try:
            dbcollection.insert_many(item_list)
            print("插入成功！")
        except Exception as e:
            print("报错：" + e.__str__())

    # 查
    def findone(self,collection, item):
        db = self.db
        dbcollection = db[collection]
        res = None
        try:
            res = dbcollection.find_one(item)

        except Exception as e:
            print("报错：" + e.__str__())

    def findall(self,collection, item):
        res = []
        db = self.db
        try:
            res = db[collection].find(item)
            print("查找成功！找到%d条结果", len(res))
        except Exception as e:
            print("报错：" + e.__str__())
        return res

    # 释放连接
    def close():
        self.client.close()
