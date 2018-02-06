#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
 Description []
 Created by yifei on 2018/2/5.
"""
import control_center

if __name__ == "__main__":
    root_url = "http://blog.csdn.net/hustqb/article/list"
    spider = control_center.SpiderMain()
    spider.start_crawling(root_url)