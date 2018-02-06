#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
 Description [爬虫调度器]
 Created by yifei on 2018/2/1.
"""
import data_collector
import resource_downloader
import resource_parser
import url_manager


class SpiderMain(object):
    def __init__(self):
        self.url_manager = url_manager.UrlManager()
        self.res_downloader = resource_downloader.ResDownloader()
        self.res_parser = resource_parser.ResParser()
        self.data_collector = data_collector.DataCollector()

    def start_crawling(self, root_url):
        count = 0
        self.url_manager.add_new_url(root_url)
        while self.url_manager.has_new_url():
            new_url = self.url_manager.get_new_url()
            print ('crawling %d : %s' % (count, new_url))
            content = self.res_downloader.downloader(new_url)
            new_urls, parsed_data = self.res_parser.parse(new_url, content)
            self.url_manager.add_new_urls(new_urls)
            self.data_collector.collect_data(parsed_data)
            count = count + 1
            if count >= 10:
                break

        self.data_collector.output_data()
