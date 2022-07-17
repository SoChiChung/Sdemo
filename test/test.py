# -*-coding:utf-8-*-
import bs4  # 网页解析
import re
import sys
import os

fatherdir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0,fatherdir+'\myvenv')
import myXlwt

headrow = ["aaa", "b", "c"]
datalist = [["a", "b", "c"], ["a2", "b2", "c2"], ["a3", "b3", "c3"]]

sheetname = "1"

book = myXlwt.mybook(headrow, sheetname, datalist)
myXlwt.savemybook("./test.xls")
