#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
 Description [数据库测试入口]
 Created by yifei on 2018/2/5.
"""

import init_db
import blogger_dao
import articleitem_dao


if __name__ == "__main__":
    host = 'localhost'
    user = 'root'
    password = 'root'
    db = 'pythontest'

    connectdb = init_db.ConnectDB(host, user, password, db)
    # todo 创建数据表
    connectdb.create_table()

    bloggerDao = blogger_dao.BloggerDao(connectdb)
    # todo 插入单条数据到blogger表中
    # bloggerDao.insert('wangwu5','www.kk.com','cccc.kaishiba.com')

    # todo 批量插入数据到blogger表中
    # params = [('zhangsan', 'ccc.zhansan.com', 'dd.zhangsan.com'),
    #           ('lisi', 'www.lisi.com', 'ccc.lisi.com')]
    # bloggerDao.insert_list(params)

    articleitemDao = articleitem_dao.ArticleItemDao(connectdb)
    # todo 插入单条数据到articleitem表中
    # articleitemDao.insert('title4', 'cccc4', 'www.ccc.com', 1)

    # todo 批量插入数据到articleitem表中
    # params = [('title3', 'cccc3', 'www.ccc.com', 5),
    #           ('title2', 'cccc2', 'www.ccc.com', 4)]
    # articleitemDao.insert_list(params)
