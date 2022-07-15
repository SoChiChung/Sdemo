# -*-coding:utf-8-*-
from bs4 import BeautifulSoup
import re

# beautifulsoup 一个可以将html解析的库

# 文件读取
file = open("F:/python/爬虫/test.html", "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")
datalist = []

# 正则
# regex = re.compile(pattern,flags = 0)

# 将正则表达式的字符串形式编译成正则表达式对象

# pattern:正则表达式的字符串或原生字符串表示

# flags:正则表达式使用时的控制标记

findlink = re.compile(r'href="(.*)')
findimgSrc = re.compile(r'src="(.*)"')
findtitles = re.compile(r'"title">(.*?)<')
findbd = re.compile(r'<p\sclass="">(.*?)</p>', re.S)
findinq=re.compile(r'class=\"inq\">(.*?)<')
findAvg=re.compile(r'v:average\">(.*)<')
find
# 直接读取标签（第一个找到的标签）
# print(bs.a)
# 读取标签内容 innerhtml
# print(bs.a.string)
for item in bs.find_all("div", attrs={"class": "item"}):
    # print(item)
    data = []
    item = str(item)
    # a = findlink.findall(t)
    link = re.findall(findlink, item)[0]
    datalist.append(link)
    imgSrc = re.findall(findimgSrc, item)[0]
    titles = re.findall(findtitles, item)
    length = len(titles)
    ctitle = titles[0]
    datalist.append(ctitle)
    if length > 1:
        datalist.append(titles[1].replace("\xa0/\xa0", ""))
    else:
        datalist.append("无")
    bd = re.findall(findbd, item)
    if len(bd) > 0:
        bd = bd[0]
        bd = re.sub("<br/>", " ", bd)
        bd = re.sub("[\n\s\xa0]", " ", bd)
    inq=re.findall(findinq, item)[0]
    avg=re.findall(findAvg, item)
    if len(avg)>0:
        print(avg[0])

    # bd.sub("<br/>")
    # print(bd)
    # print(index)
    # print(t)

    # for data in datalist:
    #     print(data)
