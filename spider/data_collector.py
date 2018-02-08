#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
 Description [数据收集，存储格式化数据]
 Created by yifei on 2018/2/1.
"""


class DataCollector(object):
    def __init__(self):
        self.datas = []

    def collect_articles(self, new_datas):
        if new_datas is None or len(new_datas) == 0:
            return

        self.datas.extend(new_datas)

    def output_data(self):
        #todo 存储到mysql中
        print(self.datas)
