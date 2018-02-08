#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
 Description []
 Created by yifei on 2018/2/7.
"""
from flask import Flask
from flask_restful import Api

from server.article_api import ArticleAPI
from server.author_api import AuthorAPI, AuthorListAPI
from server.user_api import UserAPI

app = Flask(__name__)
api = Api(app)

api.add_resource(UserAPI, '/users/<int:id>/v1', endpoint='user')
api.add_resource(AuthorAPI, 'author/v1', endpoint='author')
api.add_resource(AuthorListAPI, 'author/v1/list', endpoint='author')
api.add_resource(ArticleAPI, '/articles/v1', endpoint='articles')


class Server:
    def __init__(self):
        pass

    def run(self):
        app.run()
