#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
 Description []
 Created by yifei on 2018/2/7.
"""

from flask_restful import Resource, abort, marshal

from db import db_manager
from server.server import article_fields


class ArticleAPI(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass


class ArticleListAPI(Resource):
    def get(self):
        articleDao = db_manager.getArticleDao()
        articles = articleDao.get_list()
        if len(articles) == 0:
            return abort(204)

        return {'articles': marshal(articles, article_fields)}


