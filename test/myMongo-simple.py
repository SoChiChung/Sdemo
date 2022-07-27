"""
Author: SoChichung
Date: 2022-07-27 16:10:18
LastEditors: SoChichung
LastEditTime: 2022-07-28 02:42:34
Description: 

Copyright (c) 2022 by SoChichung ddeadwings@gmail.com, All Rights Reserved. 
"""
"""
Author: SoChichung
Date: 2022-07-27 16:10:18
LastEditors: SoChichung
LastEditTime: 2022-07-28 01:50:59
Description: 

Copyright (c) 2022 by SoChichung ddeadwings@gmail.com, All Rights Reserved. 
"""
"""
Author: SoChichung
Date: 2022-07-27 16:10:18
LastEditors: SoChichung
LastEditTime: 2022-07-28 01:40:58
Description: 

Copyright (c) 2022 by SoChichung ddeadwings@gmail.com, All Rights Reserved. 
"""

# -*- encoding: utf-8 -*-
import sys
import os
import time

print(os.path.dirname(__file__))
fatherdir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, fatherdir + "\myMongo")
from MySqlHelper import MySqlHelper

# 建立连接
db = MySqlHelper("runoobdb")
factors = {"category": "kitchen appliance"}
res = db.findall("sites", factors)
for i in res:
    print(i)
