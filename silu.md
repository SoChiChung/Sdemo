<!--
 * @Author: SoChichung
 * @Date: 2022-07-16 14:11:37
 * @LastEditors: SoChichung
 * @LastEditTime: 2022-07-16 16:46:43
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

  -
