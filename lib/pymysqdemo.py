#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/19 14:20
# Author    : smart
# @File     : pymysqdemo.py
# @Software : PyCharm
import pymysql

try:
    #建立连接
    conn = pymysql.connect(host="localhost",port=3306,
                           db="xzs",user="root",
                           password="root",charset="utf8")

    #创建一个游标对象
    cursor = conn.cursor()

    cursor.execute("select * from t_user where id=1")
    data = cursor.fetchone()
    print(data)
except Exception as e:
    print("出错了！错误信息为：{}".format(e))
finally:
    #关闭游标
    cursor.close()
    #关闭连接
    conn.close()

