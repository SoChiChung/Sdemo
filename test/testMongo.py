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

host = "localhost"
# username = "SoChichung"
# password = "1111"
# passwd = parse.quote(password)
port = "27017"
# db = "admin"

# mongo_url = (
#     "mongodb://{0}:{1}@{2}:{3}/?authSource={4}&authMechanism=SCRAM-SHA-1".format(
#         username, passwd, host, port,db
#     )
# )
mongo_url = (
    "mongodb://{0}:{1}/".format(
         host, port
    )
)
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# myclient = pymongo.MongoClient(mongo_url)
myclient=pymongo.MongoClient(host,27017)
mydb = myclient["runoobdb"]

mycol = mydb["sites"]

item_1 = {
    "_id": "U1IT00001",
    "item_name": "Blender",
    "max_discount": "10%",
    "batch_number": "RR450020FRG",
    "price": 340,
    "category": "kitchen appliance",
}

db=myclient.get_database()
# print(db.name)
print(db)
mydb.insert_one(item_1)
