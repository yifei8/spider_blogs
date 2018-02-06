#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
 Description [数据库blogger表 增/删/改/查 操作]
 Created by yifei on 2018/2/6.
"""


class BloggerDao(object):
    def __init__(self, connectdb):
        self.connected = connectdb

    def insert(self, name, avatar, url):
        db, cursor = self.connected.getCursor()
        try:
            sql = "INSERT INTO blogger(name, avatar, url) VALUES ('%s', '%s', '%s')" % (
                name, avatar, url)
            # 执行sql语句
            print('insert success ', cursor.execute(sql))
            # 执行sql语句
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()
            print(name, 'insert_one failed')
        finally:
            # 关闭游标
            cursor.close()
            # 关闭数据库连接
            db.close()

    def insert_list(self, params):
        db, cursor = self.connected.getCursor()
        try:
            sql = "INSERT INTO blogger (name, avatar, url) VALUES (%s, %s, %s)"
            # 执行sql语句
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
