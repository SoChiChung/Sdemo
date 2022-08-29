# -*- encoding: utf-8 -*-
# @File    :   spider.py
# @Time    :   2022/07/11 22:07:43
# @Author  :   So Chichung
# @Email:   ddeadwings@gmail.com


# 1.爬取网页
# 2.解析数据
# 3.保存数据
import urllib.request
import socket
import re
import os
import myXlwt
import sys
from bs4 import BeautifulSoup

fatherdir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, fatherdir + "\mymongo")
import MySqlHelper

BaseUrl = ""


def setBaseUrl(url):
    global BaseUrl
    BaseUrl = url


def getBaseUrl():
    global BaseUrl
    return BaseUrl


def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }
    # 模拟请求头

    # 构建请求 构建requset对象
    # request = urllib.request.Request(url, headers=head)
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as error:
        print("urllib.error.URLError!")
        print(error.__str__())
    except urllib.error.HTTPError as error:
        print("urllib.error.HTTPError!")
        print(error.__str__())
    except socket.timeout as error:
        print("socket.timeout!")
        print(error.__str__())
    return html


def getData(baseurl):
    datalist = []
    # (;´༎ຶД༎ຶ`)-----------------------------------( ˚ཫ˚ )-----------------------------------( ˚ཫ˚ )`)
    # 正则匹配re对象
    findlink = re.compile(r'href="(.*)"')
    findimgSrc = re.compile(r'src="(.*)"\s')
    findtitles = re.compile(r'"title">(.*?)<')
    findothers = re.compile(r'other">(.*)<')
    findbd = re.compile(r'<p\sclass="">(.*?)</p>', re.S)
    findinq = re.compile(r"class=\"inq\">(.*?)<")
    findAvg = re.compile(r"v:average\">(.*)<")
    findrating = re.compile(r"span>(\d*)人评价<\/span>")
    # ( ˚ཫ˚ )-----------------------------------( ˚ཫ˚ )-----------------------------------( ˚ཫ˚ )
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askURL(url)
        # 解析数据
        soup = BeautifulSoup(html, "html.parser")
        # print(i)
        for item in soup.find_all("div", attrs={"class": "item"}):
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
            avg = re.findall(findAvg, item)
            if len(avg) > 0:
                data.append(avg[0])
            else:
                data.append("")
            # 评分人数
            rating = re.findall(findrating, item)
            data.append(rating[0] if len(rating) > 0 else 0)
            datalist.append(data)
            # print(data.pop())
    return datalist


# 将datalist转为对线数组
def getDataToDict(baseurl):
    findlink = re.compile(r'href="(.*)"')
    findimgSrc = re.compile(r'src="(.*)"\s')
    findtitles = re.compile(r'"title">(.*?)<')
    findothers = re.compile(r'other">(.*)<')
    findinq = re.compile(r"class=\"inq\">(.*?)<")
    findAvg = re.compile(r"v:average\">(.*)<")
    findrating = re.compile(r"span>(\d*)人评价<\/span>")
    findbd = re.compile(r'<p\sclass="">(.*?)</p>', re.S)

    datalist = []
    for i in range(0, 10):
        print("当前爬取第", i + 1, "页...")
        url = baseurl + str(i * 25)
        html = askURL(url)
        # 解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", attrs={"class": "item"}):
            # print(item)
            data = {}
            item = str(item)
            # link
            link = re.findall(findlink, item)
            if len(link) > 0:
                data["link"] = link[0]
            else:
                data["link"] = ""
            # imgSrc
            imgSrc = re.findall(findimgSrc, item)
            if len(imgSrc) > 0:
                data["imgSrc"] = imgSrc[0]
            else:
                data["imgSrc"] = ""
            # title
            titles = re.findall(findtitles, item)
            length = len(titles)
            ctitle = titles[0]
            data["ctitle"] = ctitle

            if length > 1:
                data["etitle"] = titles[1].replace("\xa0/\xa0", "")
            else:
                data["etitle"] = "无"
            # others
            others = re.findall(findothers, item)[0]
            data["others"] = others.replace("\xa0/\xa0", "")
            # print(
            # "(;´༎ຶД༎ຶ`)-----------------------------------( ˚ཫ˚ )-----------------------------------( ˚ཫ˚ )`)"
            # )

            # 信息
            bd = re.findall(findbd, item)

            if len(bd) > 0:
                bd = bd[0]
                bd = re.sub("<br/>\s*", " ", bd)
                bd = re.sub("[\n\s\xa0]", " ", bd)
                data["bd"] = bd.strip()
            else:
                data["bd"] = ""
            # 一句话评价
            inq = re.findall(findinq, item)
            if len(inq) > 0:
                data["inq"] = inq[0]
            else:
                data["inq"] = ""

            # 平均分
            avg = re.findall(findAvg, item)
            if len(avg) > 0:
                data["avg"] = avg[0]
            else:
                data["avg"] = ""
            # 评分人数
            rating = re.findall(findrating, item)
            data["rating"] = rating[0] if len(rating) > 0 else 0
            datalist.append(data)

    return datalist


def saveData(savepath, type: int, datalist):  # 传入参数 type：1 代表用Excel 2代表用数据库
    if type == 1:
        saveDataByExcel(savepath, datalist)
    elif type == 2:
        saveDataByMongo(savepath, datalist)
    return


def saveDataByExcel(savepath, datalist):  # headrow就自己写了 不传参了
    headrow = ["链接", "插图地址", "中文片名", "英文片名", "其他片名", "详情", "简评", "评分", "打分人数"]
    book = myXlwt.mybook(headrow, "1", datalist)
    myXlwt.savemybook(savepath)


# getMongoDatabase
def getMongoDatabase(dbname):
    db = MySqlHelper.SqlHelper("doubanmovie")
    return db


if __name__ == "__main__":

    setBaseUrl("https://movie.douban.com/top250?start=")
    baseurl = getBaseUrl()
    print(dir(MySqlHelper))
    # setSavepath(".\\豆瓣电影TOP250.xls")
    # savepath = getSavepath()
    # 1.爬取网页
    # askURL(baseurl + "")

    # 2.解析数据
    # datalist = getData(baseurl)
    datalist = getDataToDict(baseurl)
    # for data in datalist:
    # print(data)
    # 3.保存数据
    # 通过excel保存
    # savepath = os.path.dirname(__file__) + "/output/豆瓣电影TOP250.xls"
    # saveData(savepath, 1, datalist)

    # save data into mongo
    db = getMongoDatabase("doubanmovie")
    db.insert_many("top250", datalist)
