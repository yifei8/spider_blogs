#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
 Description [资源解析器]
 Created by yifei on 2018/2/1.
"""
import re
from bs4 import BeautifulSoup


class ResParser(object):
    def parse(self, url, content):
        if url is None or content is None:
            return
        soup = BeautifulSoup(content, features="html.parser", from_encoding="utf-8")
        data = self._get_data(url, soup)
        return data

    '''
<li class="blog-unit">
	<a href="http://blog.csdn.net/mwq384807683/article/details/71435960" "="" target="_blank">
    	<h3 class="blog-title odd-overhidden bottom-dis-8">
						<span class="top">置顶</span>
        				面试题-史上最全人事面试宝典		</h3>
        <p class="text bottom-dis-8">人事面试宝典</p>
        
	</a>
</li>
    '''

    def _get_data(self, root_url, soup):
        data = []
        subdata = {}
        lis = soup.find_all('li', class_="blog-unit")
        for li in lis:
            subdata['sources_url'] = root_url
            a = li.find('a')
            subdata['href'] = a['href']
            h3 = li.find('h3', class_="blog-title odd-overhidden bottom-dis-8")
            subdata['title'] = h3.get_text().encode('utf-8')
            data.append(subdata)

        return data
