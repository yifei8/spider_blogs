#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
 Description [数据收集，存储格式化数据]
 Created by yifei on 2018/2/1.
"""


class DataCollector(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_data(self):
        #todo 以json 格式存储到文件
        print(self.datas)
