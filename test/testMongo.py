"""
Author: SoChichung
Date: 2022-07-17 19:57:28
LastEditors: SoChichung
LastEditTime: 2022-07-27 22:29:06
Description: 

Copyright (c) 2022 by SoChichung ddeadwings@gmail.com, All Rights Reserved. 
"""
"""
Author: SoChichung
Date: 2022-07-17 19:57:28
LastEditors: SoChichung
LastEditTime: 2022-07-27 21:38:35
Description: 

Copyright (c) 2022 by SoChichung ddeadwings@gmail.com, All Rights Reserved. 
"""
"""
Author: SoChichung
Date: 2022-07-17 19:57:28
LastEditors: SoChichung
LastEditTime: 2022-07-26 22:19:47
Description: :

Copyright (c) 2022 by SoChichung ddeadwings@gmail.com, All Rights Reserved. 
"""


# -*- encoding: utf-8 -*-
import pymongo
from urllib import parse
import time

host = "localhost"
username = "myUserAdmin"
password = "aahph"
passwd = parse.quote(password)
port = "27017"
# db = "admin"

mongo_url = "mongodb://{0}:{1}@{2}:{3}/".format(username, passwd, host, port)
# mongo_url = "mongodb://{0}:{1}/".format(host, port)
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myclient = pymongo.MongoClient(mongo_url)
# myclient = pymongo.MongoClient(host, 27017)

mydb = myclient["runoobdb"]

s = "sites"
mycol = mydb[s]
# myclient.admin.aurhenticate()
# mydb.command("createUser", "admin", pwd="111", roles=["dbAdmin"])
# mycol = mydb["sites"]
timestamp = time.time()  # 时间戳
item_1 = {
    "_id": "U1IT00001" + str(timestamp),
    "item_name": "Blender",
    "max_discount": "10%",
    "batch_number": "RR450020FRG",
    "price": 340,
    "category": "kitchen appliance",
    "timestamp": timestamp,
}
item_2 = {
    "_id": "U1IT00001",
    "item_name": "Blender",
    "max_discount": "10%",
    "batch_number": "RR450020FRG",
    "price": 340,
    "category": "kitchen appliance",
}

factors = {"category": "kitchen appliance"}
print(mycol)
r = mycol.find(factors)

for i in r:
    print(i)
# db = myclient.get_database()
# print(db.name)
# print(db)
# mydb.insert(item_1) #insert_one 这个方法是用在db的collection里面的
# try:
#     mycol.insert_one(item_1)
#     print("插入成功！")
# except Exception as e:
#     print("报错：" + e.__str__())

myclient.close()
