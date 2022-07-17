"""
Author: SoChichung
Date: 2022-07-16 02:22:44
LastEditors: SoChichung
LastEditTime: 2022-07-16 16:02:53
Description: 

Copyright (c) 2022 by SoChichung ddeadwings@gmail.com, All Rights Reserved. 
"""
# -*- encoding: utf-8 -*-
import xlwt

# testbook=xlwt.Workbook()#book对象（工作簿）
# testsheet=testbook.add_sheet('test')#(工作表)
# testsheet.write(0, 0, 1234.56)

# testbook.save('test.xls')#(保存)
global book


def mybook(headrow:list,sheetname: str, datalist: list):
    global book
    book = xlwt.Workbook()
    sheet = book.add_sheet(sheetname)
    l = len(datalist)
    for i in range(len(headrow)):
        sheet.write(0,i,headrow[i])
    for row in range(l):
        for col in range(len(datalist[row])):
            sheet.write(row+1,col,datalist[row][col])#从第二行开始写



def savemybook(savepath: str):
    global book
    book.save(savepath)
