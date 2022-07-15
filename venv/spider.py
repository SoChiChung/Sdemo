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
from bs4 import BeautifulSoup

BaseUrl = ""
Savepath = ""


def setBaseUrl(url):
    global BaseUrl
    BaseUrl = url


def getBaseUrl():
    global BaseUrl
    return BaseUrl


def setSavepath(savepath):
    global Savepath
    Savepath = savepath


def getSavepath():
    global Savepath
    return Savepath


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
    for i in range(0, 2):
        url = baseurl + str(i * 2)
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
            datalist.append(data)
            avg = re.findall(findAvg, item)
            if len(avg) > 0:
                data.append(avg[0])
            else:
                data.append("")
            # 评分人数
            rating = re.findall(findrating, item)
            data.append(rating[0] if len(rating) > 0 else 0)

            # print(data.pop())
    return datalist


def saveData(savepath):
    return


if __name__ == "__main__":

    setBaseUrl("https://movie.douban.com/top250?start=")
    baseurl = getBaseUrl()
    setSavepath(".\\豆瓣电影TOP250.xls")
    savepath = getSavepath()
    saveData(savepath)
    # 1.爬取网页
    datalist = getData(baseurl)
    # for data in datalist:
    #     print(data)
    # 2.解析数据

    # 3.保存数据
    # askURL(baseurl + "")
