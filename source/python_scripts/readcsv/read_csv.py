#!/usr/bin/python3                                                                                                                                                      
# -*- coding: utf-8 -*-
# ----------------------------------------------------------
# @Time          : At 下午9:25 九月 10, 2018 
# @Author        : 梅朝辉(meizhaohui)
# @Email         : mzh@hopewait.com
# @Filename      : read_csv.py
# @Description   : 读取csv文件
# @Software      : PyCharm
# @Python Version: python3.6.2
# ----------------------------------------------------------

import csv
CSV_FILE = 'file.csv'
CSV_DATA = [
    ['id', 'username', 'age', 'country'],
    ['1001', 'Stephen Curry', '30', 'USA'],
    ['1002', 'Kobe Bryant', '40', 'USA'],
    ['1003', 'Manu Ginóbili', '41', 'Argentina']
    ]


def read_csv_file(csv_file_path=None):
    """
    读取csv文件
    :param csv_file_path: csv文件路径
    :return:
    """
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        # 读取csv文件
        rows = csv.reader(csv_file)
        # 读取第1行的表头
        head_row = next(rows)
        print(rows.line_num, head_row)
        # 从第2行开始读取
        for row in rows:
            print(rows.line_num, row)


if __name__ == '__main__':
    read_csv_file(CSV_FILE)
