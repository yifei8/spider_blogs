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
        db, cursor = self.connected.getCursor()
        try:
            sql = "INSERT INTO article(href, des, author_slug, title) VALUES (%(href)s, %(des)s, %(author_slug)s, %(title)s)"

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

    def get_list(self):
        db, cursor = self.connected.getCursor()
        data = []
        try:
            sql = "select * from article"
            cursor.execute(sql)
            rows = cursor.fetchall()
            fields = cursor.description
            print type(fields)
            column_list = []
            for i in fields:
                column_list.append(i[0])
            # 执行sql语句
            print('get_list success')
            for row in rows:
                result = {}
                result[column_list[0]] = row[0]
                result[column_list[1]] = str(row[1])
                result[column_list[2]] = str(row[2])
                result[column_list[3]] = row[3]
                result[column_list[4]] = str(row[4])
                data.append(result)

            # 执行sql语句
            db.commit()
        except IndentationError as e:
            # 发生错误时回滚
            db.rollback()
            print('get_list failed', e)
        finally:
            # 关闭游标
            cursor.close()
            # 关闭数据库连接
            db.close()
            return data
