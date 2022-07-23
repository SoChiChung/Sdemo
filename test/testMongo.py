"""
Author: SoChichung
Date: 2022-07-17 19:57:28
LastEditors: SoChichung
LastEditTime: 2022-07-23 06:08:59
Description: 

Copyright (c) 2022 by SoChichung ddeadwings@gmail.com, All Rights Reserved. 
"""
"""
Author: SoChichung
Date: 2022-07-17 19:57:28
LastEditors: SoChichung
LastEditTime: 2022-07-23 04:01:08
Description: 

Copyright (c) 2022 by SoChichung ddeadwings@gmail.com, All Rights Reserved. 
"""
"""
Author: SoChichung
Date: 2022-07-17 19:57:28
LastEditors: SoChichung
LastEditTime: 2022-07-20 22:22:22
Description: 

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
# myclient.admin.aurhenticate()
# mydb.command("createUser", "admin", pwd="111", roles=["dbAdmin"])
mycol = mydb["sites"]
timestamp = time.time()  # 时间戳
item_1 = {
    "_id": "U1IT00001" + str(timestamp),
    "item_name": "Blender",
    "max_discount": "10%",
    "batch_number": "RR450020FRG",
    "price": 340,
    "category": "kitchen appliance",
}

# db = myclient.get_database()
# print(db.name)
# print(db)
# mydb.insert(item_1) #insert_one 这个方法是用在db的collection里面的
mycol.insert_one(item_1)

myclient.close()
