"""
Author: SoChichung
Date: 2022-06-28 00:02:21
LastEditors: SoChichung
LastEditTime: 2022-08-07 06:48:22
Description: 

Copyright (c) 2022 by SoChichung ddeadwings@gmail.com, All Rights Reserved. 
"""
"""
Author: SoChichung
Date: 2022-06-28 00:02:21
LastEditors: SoChichung
LastEditTime: 2022-07-17 15:46:58
Description: 

Copyright (c) 2022 by SoChichung ddeadwings@gmail.com, All Rights Reserved. 
"""
# -*-coding:utf-8-*-
import bs4  # 网页解析
import re
import sys
import os

import time
fatherdir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))#父目录
sys.path.insert(0, fatherdir + "\myvenv")
import myXlwt

headrow = ["aaa", "b", "c"]
datalist = [["a", "b", "c"], ["a2", "b2", "c2"], ["a3", "b3", "c3"]]

sheetname = "1"

book = myXlwt.mybook(headrow, sheetname, datalist)
myXlwt.savemybook("./test.xls")

# t = time.time()
# a = []
# a["b"] = 1


# class test(a):
#     def __init__(self):
#         self.a = a


# b = "b"
# print(a["b"])
# print(a[0])
# print(a[int(b)])
