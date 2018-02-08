#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
 Description []
 Created by yifei on 2018/2/7.
"""
from flask import Flask
from flask_restful import Api

from server.article_api import ArticleAPI
from server.blogger_api import BloggerAPI
from server.user_api import UserAPI

app = Flask(__name__)
api = Api(app)

api.add_resource(UserAPI, '/users/<int:id>', endpoint='user')
api.add_resource(BloggerAPI, '/v1.0/blogger', endpoint='blogger')
api.add_resource(ArticleAPI, '/v1.0/articles', endpoint='articles')


class Server:
    def __init__(self):
        pass

    def run(self):
        app.run()
