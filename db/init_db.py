#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
 Description [数据库连接]
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

    def create_table(self):
        db, cursor = self.getCursor()
        try:
            # todo 创建 user 表
            cursor.execute('DROP TABLE IF EXISTS user')
            create_user_table_sql = '''
                                       CREATE TABLE IF NOT EXISTS `user` (
                                         `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
                                         `name` varchar(50) NOT NULL,
                                         `pwd` varchar(20) NOT NULL,
                                         PRIMARY KEY (`id`)
                                       ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
                                       '''
            # 执行sql语句
            print(create_user_table_sql)
            print('create user table success ', cursor.execute(create_user_table_sql))

            # todo 创建 author 表
            cursor.execute('DROP TABLE IF EXISTS author')
            create_author_table_sql = '''
                           CREATE TABLE IF NOT EXISTS `author` (
                             `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
                             `slug` varchar(40) DEFAULT NULL,
                             `name` varchar(40) DEFAULT NULL,
                             `avatar` tinytext,
                             `url` text,
                             PRIMARY KEY (`id`)
                           ) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
                           '''
            print(create_author_table_sql)
            print('create article table success ', cursor.execute(create_author_table_sql))

            # todo 创建 article 表
            cursor.execute('DROP TABLE IF EXISTS article')
            create_article_table_sql = '''
                           CREATE TABLE IF NOT EXISTS `article` (
                             `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
                             `title` tinytext,
                             `des` text,
                             `href` text NOT NULL,
                             `author_slug` int(11) DEFAULT NULL,
                             PRIMARY KEY (`id`),
                             KEY `author_slug` (`author_slug`)
                           ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
                           '''
            # 执行sql语句
            print(create_article_table_sql)
            print('create article table success ', cursor.execute(create_article_table_sql))
            # 执行sql语句
            db.commit()
        except IndentationError as e:
            # 发生错误时回滚
            db.rollback()
            print('create table failed', e)
        finally:
            # 关闭游标
            cursor.close()
            # 关闭数据库连接
            db.close()
