#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import urlparse

if __name__ == "__main__":
    url = 'http://blog.csdn.net/hustqb/article/list'
    up = urlparse.urlparse(url)
    if 'blog.csdn.net' == up.hostname:
        print 'yes'
        print up.path
        print up.path.split(r'/')
        print up.path.split(r'/')[1]
    else:
        print 'no'

