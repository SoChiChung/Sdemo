<!--
 * @Author: SoChichung
 * @Date: 2022-07-16 14:11:37
 * @LastEditors: SoChichung
 * @LastEditTime: 2022-07-21 21:44:17
 * @Description:
 *
 * Copyright (c) 2022 by SoChichung ddeadwings@gmail.com, All Rights Reserved.
-->

# 思路汇总

### xlwt 测试环境的搭建思路

- 封装方法：

  - 封装一个 _workbook_ 的对象 输入参数 _sheetnamelist_ _headrow_ _datalist_ 根据数据写列表
    - _sheetnamelist_:一个字符串就好了 只用作定义 _sheet_ 的名称
    - _headrow_ ：一个定义首行字段的数组
    - _datalist_:一个二维数组 包含爬取的数据 不包含第一行的题头
  - 封装一个 _save_ 方法 输入参数 _savepath_ 保存工作簿

### **_pymongo_** 环境搭建思路

- 封装一个 _getPmongo_ 类
  - 建立 Mongo 连接
  - 根据 DB name 建立对应的 db 对象（代表数据库）
    - 包含 对文档的 crud 的封装
  * 添加对 db 的 crud 操作的封装方法

* 每次 _insert_ 加入时间戳
