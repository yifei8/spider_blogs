#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
 Description []
 Created by yifei on 2018/2/7.
"""
from flask_restful import Resource, reqparse, fields, marshal, abort

user_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'pwd': fields.String
}

users = [
    {
        'id': 1,
        'name': '张三',
        'pwd': '123356',
    },
    {
        'id': 2,
        'name': '李四',
        'pwd': '123356',
    }
]


class UserAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, required=True,
                                   help='No user name provided', location='json')
        self.reqparse.add_argument('pwd', type=str, required=True,
                                   help='No password provided', location='json')
        super(UserAPI, self).__init__()

    def get(self, user_id):
        user = filter(lambda t: t['id'] == user_id, users)
        if len(user) == 0:
            abort(404)
        return {'user': marshal(user, user)}, 201

    def put(self, id):
        pass

    def delete(self, id):
        pass
