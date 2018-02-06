#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
 Description [数据库测试入口]
/*
 Navicat MySQL Data Transfer

 Source Server         : python
 Source Server Type    : MySQL
 Source Server Version : 50720
 Source Host           : localhost
 Source Database       : pythontest

 Target Server Type    : MySQL
 Target Server Version : 50720
 File Encoding         : utf-8

 Date: 02/06/2018 14:14:27 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `articleitem`
-- ----------------------------
DROP TABLE IF EXISTS `articleitem`;
CREATE TABLE `articleitem` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `title` tinytext,
  `des` text,
  `url` text NOT NULL,
  `author_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `author_id` (`author_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

SET FOREIGN_KEY_CHECKS = 1;

-- ----------------------------
--  Table structure for `blogger`
-- ----------------------------
DROP TABLE IF EXISTS `blogger`;
CREATE TABLE `blogger` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `avatar` tinytext,
  `url` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

SET FOREIGN_KEY_CHECKS = 1;

 Created by yifei on 2018/2/5.
"""

import connect_db
import blogger_dao
import articleitem_dao

if __name__ == "__main__":
    host = 'localhost'
    user = 'root'
    password = 'root'
    db = 'pythontest'

    connectdb = connect_db.ConnectDB(host, user, password, db)

    # bloggerDao = blogger_dao.BloggerDao(connectdb)
    # 插入单条数据到blogger表中
    # bloggerDao.insert('wangwu5','www.kk.com','cccc.kaishiba.com')

    # 批量插入数据到blogger表中
    # params = [('zhangsan', 'ccc.zhansan.com', 'dd.zhangsan.com'),
    #           ('lisi', 'www.lisi.com', 'ccc.lisi.com')]
    # bloggerDao.insert_list(params)

    articleitemDao = articleitem_dao.ArticleItemDao(connectdb)
    # 插入单条数据到articleitem表中
    # articleitemDao.insert('title4', 'cccc4', 'www.ccc.com', 1)

    # 批量插入数据到articleitem表中
    params = [('title3', 'cccc3', 'www.ccc.com', 5),
              ('title2', 'cccc2', 'www.ccc.com', 4)]
    articleitemDao.insert_list(params)
