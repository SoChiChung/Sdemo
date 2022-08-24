"""
Author: SoChichung
Date: 2022-06-28 10:58:05
LastEditors: SoChichung
LastEditTime: 2022-08-24 00:18:39
Description: 

Copyright (c) 2022 by SoChichung ddeadwings@gmail.com, All Rights Reserved. 
"""
# 测试urllib
# -*-coding:utf-8-*-
import urllib.request
import socket

# get 请求
# response = urllib.request.urlopen("https://movie.douban.com/top250")
# print(response.read().decode("utf-8"))

# post 请求
url = "http://httpbin.org/post"

import urllib.parse

# 用bytes（）方法传参

# data = bytes(urllib.parse.urlencode({"DYS": "AAHPH"}), encoding="utf-8")
# response = urllib.request.urlopen(url, data)
# print(response.read().decode("utf-8"))

# 用try catch 捕获异常

# try:
#     data = bytes(urllib.parse.urlencode({"DYS": "AAHPH"}), encoding="utf-8")
#     response = urllib.request.urlopen(url, timeout=0.1)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as error:
#     print("urllib.error.URLError!")
#     print(error.__str__())
# except urllib.error.HTTPError as error:
#     print("urllib.error.HTTPError!")
#     print(error.__str__())
# except socket.timeout as error:
#     print("socket.timeout!")
#     print(error.__str__())

# 状态码
# 418：爬虫被发现

# 封装request

data = bytes({})
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
res = urllib.request.Request("https://movie.douban.com/top250", data, headers)
response = urllib.request.urlopen(res)
print(response.read().decode("utf-8"))
