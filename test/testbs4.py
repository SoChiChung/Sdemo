"""
Author: SoChichung
Date: 2022-06-28 23:03:30
LastEditors: SoChichung
LastEditTime: 2022-07-16 16:55:11
Description: 

Copyright (c) 2022 by SoChichung ddeadwings@gmail.com, All Rights Reserved. 
"""
# -*-coding:utf-8-*-
from bs4 import BeautifulSoup
import re
import sys
import os

fatherdir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, fatherdir + "\myvenv")
import myXlwt

# beautifulsoup 一个可以将html解析的库

# 文件读取
filepath = fatherdir + "/test.html"
file = open(filepath, "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")
datalist = []

# 正则
# regex = re.compile(pattern,flags = 0)

# 将正则表达式的字符串形式编译成正则表达式对象

# pattern:正则表达式的字符串或原生字符串表示

# flags:正则表达式使用时的控制标记

findlink = re.compile(r'href="(.*)"')
findimgSrc = re.compile(r'src="(.*)"\s')
findtitles = re.compile(r'"title">(.*?)<')
findothers = re.compile(r'other">(.*)<')
findbd = re.compile(r'<p\sclass="">(.*?)</p>', re.S)
findinq = re.compile(r"class=\"inq\">(.*?)<")
findAvg = re.compile(r"v:average\">(.*)<")
findrating = re.compile(r"span>(\d*)人评价<\/span>")

# 直接读取标签（第一个找到的标签）
# print(bs.a)
# 读取标签内容 innerhtml
# print(bs.a.string)
for item in bs.find_all("div", attrs={"class": "item"}):
    # print(item)
    data = []
    item = str(item)
    # link
    link = re.findall(findlink, item)
    if len(link) > 0:
        data.append(link[0])
    else:
        data.append("")
    # imgSrc
    imgSrc = re.findall(findimgSrc, item)
    if len(imgSrc) > 0:
        data.append(imgSrc[0])
    else:
        data.append("")
    # title
    titles = re.findall(findtitles, item)
    length = len(titles)
    ctitle = titles[0]
    data.append(ctitle)
    if length > 1:
        data.append(titles[1].replace("\xa0/\xa0", ""))
    else:
        data.append("无")
    # others
    others = re.findall(findothers, item)[0]
    data.append(others.replace("\xa0/\xa0", ""))
    # print(
    # "(;´༎ຶД༎ຶ`)-----------------------------------( ˚ཫ˚ )-----------------------------------( ˚ཫ˚ )`)"
    # )

    # 信息
    bd = re.findall(findbd, item)
    if len(bd) > 0:
        bd = bd[0]
        bd = re.sub("<br/>\s*", " ", bd)
        bd = re.sub("[\n\s\xa0]", " ", bd)
        data.append(bd.strip())
    else:
        data.append("")
    # 一句话评价
    inq = re.findall(findinq, item)
    if len(inq) > 0:
        data.append(inq[0])
    else:
        data.append("")

    # 平均分
    datalist.append(data)
    avg = re.findall(findAvg, item)
    if len(avg) > 0:
        data.append(avg[0])
    else:
        data.append("")
    # 评分人数
    rating = re.findall(findrating, item)
    data.append(rating[0] if len(rating) > 0 else 0)
    datalist.append(data)
# for data in datalist:
#     print(data)

# Excel 保存
headrow = ["链接", "插图地址", "中文片名", "英文片名", "其他片名", "详情", "简评", "评分", "打分人数"]
book = myXlwt.mybook(headrow, "1", datalist)
myXlwt.savemybook(os.path.dirname(__file__) + "/test.xls")
