#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/23 11:42
# Author    : smart
# @File     : read_excel.py
# @Software : PyCharm
import xlrd

class readexcel():

    def excel_to_list(self,data_file, sheet):
        wb = xlrd.open_workbook(data_file)
        sheet1 = wb.sheet_by_name(sheet)
        #获取第一行的数据
        keys = sheet1.row_values(0)
        list1 = []
        #从第二行开始获取数据
        for i in range(1, sheet1.nrows):
            j = dict(zip(keys, sheet1.row_values(i)))
            list1.append(j)
        return list1

    def get_test_data(self,data_list, case_name):
        for case_data in data_list:
            if case_name == case_data['case_name']:
                return case_data  # 如果查询不到会返回None

if __name__ == '__main__':
    r=readexcel()
    print(r.excel_to_list("test_user_data.xlsx","test_user_login"))

