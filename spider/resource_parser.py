#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
 Description [资源解析器]
 Created by yifei on 2018/2/1.
"""
import re
import urlparse

from bs4 import BeautifulSoup


class ResParser(object):
    def parse(self, url, content):
        if url is None or content is None:
            return
        soup = BeautifulSoup(content, features="html.parser", from_encoding="utf-8")
        data = self._get_data(url, soup)
        new_urls = self._get_new_urls(url, soup)
        return new_urls, data

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

        slug = self._get_slug(root_url)
        lis = soup.find_all('li', class_="blog-unit")
        for li in lis:
            subdata = {}
            a = li.find('a')
            subdata['href'] = a['href']
            h3 = li.find('h3', class_="blog-title odd-overhidden bottom-dis-8")
            subdata['title'] = ''.join(h3.text.split())
            p = li.find('p', class_="text bottom-dis-8")
            subdata['des'] = ''.join(p.text.split())
            subdata['author_slug'] = slug
            # print subdata['title']
            data.append(subdata)

        print data
        return data

    def _get_new_urls(self, root_url, soup):
        new_urls = set()
        # <a href="http://blog.csdn.net/mwq384807683/article/list/2" class="page-link" data-ci-pagination-page="2">2</a>
        lis = soup.find_all('a', class_="page-link")
        for li in lis:
            try:
                new_url = li['href']
                new_urls.add(new_url)
            except:
                pass

        return new_urls

    def _get_slug(self, url):
        up = urlparse.urlparse(url)
        if 'blog.csdn.net' == up.hostname:
            return up.path.split(r'/')[1]
        return ''
