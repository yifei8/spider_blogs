#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
 Description [数据库article表 增/删/改/查 操作]
 Created by yifei on 2018/2/6.
"""


class ArticleDao:
    def __init__(self, connectdb):
        self.connected = connectdb

    def insert(self, title, des, url, author_id):
        db, cursor = self.connected.getCursor()
        try:
            sql = "INSERT INTO article(title, des, url, author_id) VALUES ('%s', '%s', '%s', '%d')" % (
                title, des, url, author_id)
            # 执行sql语句
            print('insert success ', cursor.execute(sql))
            # 执行sql语句
            db.commit()
        except IndentationError as e:
            # 发生错误时回滚
            db.rollback()
            print(title, 'insert_one failed', e)
        finally:
            # 关闭游标
            cursor.close()
            # 关闭数据库连接
            db.close()

    def insert_list(self, params):
        '''
        [(
        	'href': u 'http://blog.csdn.net/hustqb/article/details/77869076',
        	'des': u '看完本教程，就可以应付大多数情况下的柱状图绘制了。',
        	'slug': 'hustqb',
        	'title': u '图文并茂的Python散点图教程'
        ),(
        	'href': u 'http://blog.csdn.net/hustqb/article/details/77869076',
        	'des': u '看完本教程，就可以应付大多数情况下的柱状图绘制了。',
        	'slug': 'hustqb',
        	'title': u '图文并茂的Python散点图教程'
        )]
        '''
        db, cursor = self.connected.getCursor()
        try:
            sql = "INSERT INTO article(href, des, author_slug, title) VALUES (%(href)s, %(des)s, %(author_slug)s, %(title)s)"

            # 执行sql语句
            print(params)
            print('insert list success ', cursor.executemany(sql, params))
            # 执行sql语句
            db.commit()
        except IndentationError as e:
            # 发生错误时回滚
            db.rollback()
            print('insert_list failed', e)
        finally:
            # 关闭游标
            cursor.close()
            # 关闭数据库连接
            db.close()
