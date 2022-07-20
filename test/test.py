"""
Author: SoChichung
Date: 2022-06-28 00:02:21
LastEditors: SoChichung
LastEditTime: 2022-07-20 22:48:35
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

print(os.path.dirname(__file__))
fatherdir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, fatherdir + "\myvenv")
import myXlwt

headrow = ["aaa", "b", "c"]
datalist = [["a", "b", "c"], ["a2", "b2", "c2"], ["a3", "b3", "c3"]]

sheetname = "1"

book = myXlwt.mybook(headrow, sheetname, datalist)
# myXlwt.savemybook("./test.xls")
