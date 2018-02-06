#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
 Description [url 链接管理器]
 Created by yifei on 2018/2/1.
"""


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        if len(self.new_urls) == 0:
            return False
        return True

    def get_new_url(self):
        if len(self.new_urls) == 0:
            return None
        url = self.new_urls.pop()
        self.old_urls.add(url)
        return url
