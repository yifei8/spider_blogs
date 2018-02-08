#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
 Description [数据库测试入口]
 Created by yifei on 2018/2/5.
"""

import db_manager
import author_dao
import article_dao


if __name__ == "__main__":
    host = 'localhost'
    user = 'root'
    password = 'root'
    db = 'pythontest'

    connectdb = db_manager.ConnectDB(host, user, password, db)
    # todo 创建数据表
    # connectdb.create_table()

    authorDao = author_dao.AuthorDao(connectdb)
    # todo 插入单条数据到author表中
    # authorDao.insert('wangwu5','www.kk.com','cccc.kaishiba.com')

    # todo 批量插入数据到author表中
    # params = [('zhangsan', 'ccc.zhansan.com', 'dd.zhangsan.com'),
    #           ('lisi', 'www.lisi.com', 'ccc.lisi.com')]
    # authorDao.insert_list(params)

    articleDao = article_dao.ArticleDao(connectdb)
    # todo 插入单条数据到articleitem表中
    # articleDao.insert('title4', 'cccc4', 'www.ccc.com', 1)

    # todo 批量插入数据到articleitem表中
    # params = [('title3', 'cccc3', 'www.ccc.com', 5),
    #           ('title2', 'cccc2', 'www.ccc.com', 4)]
    # articleDao.insert_list(params)

    # todo 查询article 表
    articleDao.get_list()
