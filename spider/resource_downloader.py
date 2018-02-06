#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
 Description [资源下载器]
 Created by yifei on 2018/2/1.
"""
import urllib2

class ResDownloader(object):
    def downloader(self, url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
