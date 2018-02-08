#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
 Description []
 Created by yifei on 2018/2/7.
"""
from flask import Flask, make_response, jsonify
from flask_restful import Api, fields

from server.article_api import ArticleAPI, ArticleListAPI
from server.author_api import AuthorAPI, AuthorListAPI
from server.user_api import UserAPI

app = Flask(__name__)
api = Api(app)

api.add_resource(UserAPI, '/users/<int:id>/v1', endpoint='user')
api.add_resource(AuthorAPI, 'author/v1', endpoint='author')
api.add_resource(AuthorListAPI, 'author/v1/list', endpoint='author')
api.add_resource(ArticleAPI, '/articles/v1', endpoint='articles')
api.add_resource(ArticleListAPI, '/articles/v1', endpoint='articles')


@app.errorhandler(204)
def not_found(error):
    return make_response(jsonify({'error': 'No Content'}), 204)


@app.errorhandler(403)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# 生成响应，把来自原始服务器上的任务从内部形式包装成客户端想要的外部形式
article_fields = {
    'title': fields.String,
    'des': fields.String,
    'href': fields.String,
    'author_slug': fields.String
}

class Server:
    def run(self):
        app.run(debug=True)
