#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/18 14:51
# Author    : smart
# @File     : testlogin.py
# @Software : PyCharm
import unittest
from lib import xzs_testlogin


class MyTestCase(unittest.TestCase):
    x= xzs_testlogin.xzs_login()
    def test_login_ok(self):
        t = self.x.login("admin","123456")
        self.assertIn("成功",t)
    def test_login_err01(self):
        t = self.x.login("", "123456")
        self.assertIn("用户名或密码错误",t)
    def test_login_err02(self):
        t = self.x.login("admin", "")
        self.assertIn("用户名或密码错误",t)

if __name__ == '__main__':
    unittest.main()


