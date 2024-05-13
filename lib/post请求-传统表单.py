#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/15 15:35
# Author    : smart
# @File     : post请求-传统表单.py
# @Software : PyCharm
import requests

url = "http://httpbin.org/post"


data = {
    "name":"zhangsan",
    "age":"18"
}

headers = {
    "content-type":"x-www-form-urlencoded"
}
#传统默认表单
r = requests.post(url=url,headers=headers,data=data)

print(r.text)