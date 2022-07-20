"""
Author: SoChichung
Date: 2022-07-17 19:57:28
LastEditors: SoChichung
LastEditTime: 2022-07-20 22:22:22
Description: 

Copyright (c) 2022 by SoChichung ddeadwings@gmail.com, All Rights Reserved. 
"""
"""
Author: SoChichung
Date: 2022-07-17 19:57:28
LastEditors: SoChichung
LastEditTime: 2022-07-18 20:42:56
Description: 

Copyright (c) 2022 by SoChichung ddeadwings@gmail.com, All Rights Reserved. 
"""
# -*- encoding: utf-8 -*-
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
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

# mycol.insert_one(item_1)
