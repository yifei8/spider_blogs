#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
 Description []
 Created by yifei on 2018/2/6.
"""

import pymysql


class ConnectDB:
    def __init__(self, host, user, password, dbname, charset='utf8mb4'):
        self.host = host
        self.user = user
        self.password = password
        self.db = dbname
        self.charset = charset

    # 打开数据库连接
    def _getDB(self):
        db = pymysql.Connect(host=self.host, user=self.user, password=self.password, db=self.db, charset=self.charset)
        return db

    # 获取会话指针 使用cursor()方法获取操作游标
    def getCursor(self):
        db = self._getDB()
        cursor = db.cursor()
        return db, cursor
