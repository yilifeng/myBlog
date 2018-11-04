#!/usr/bin/env python
# coding:utf-8

from flask import Blueprint
from ..common import log
from ..model import blog_user
from flask import jsonify
from flask import request

logger = log.get_logger()

blueprint = Blueprint("user", __name__, url_prefix="/user")


@blueprint.route('/<id>', methods=['GET'])
def get_one(id):
    data = blog_user.get_one({"id": id})
    if data:
        logger.debug("get test info: {}".format(data))
        return jsonify({"status": 0, "data": data})
    else:
        return jsonify({"status": 0, "data": []})


@blueprint.route('/', methods=['GET'])
def get_all():
    data = blog_user.get_one()
    if data:
        logger.debug("get test info: {}".format(data))
        return jsonify({"status": 0, "data": data})
    else:
        return jsonify({"status": 0, "data": []})


@blueprint.route('/', methods=['POST'])
def create():
    data = request.get_json(force=True)
    if not (isinstance(data, dict)):
        logger.error("create test, data is not dict: data {}".format(data))

    res = blog_user.create_user(data)
    if res:
        return jsonify({"code": 0})
    return jsonify({"code": 10001})


@blueprint.route('/', methods=['DELETE'])
def delete_test():
    data = request.get_json(force=True)
    if not (isinstance(data, dict)):
        logger.error("create test, data is not dict: data {}".format(data))

    res = blog_user.delete_one(data)
    if res:
        return jsonify({"code": 0})
    return jsonify({"code": 10001})


@blueprint.route('/<id>', methods=['DELETE'])
def delete_one_test(id):
    res = blog_user.delete_one({"id": id})
    if res:
        return jsonify({"code": 0})
    return jsonify({"code": 10001})


@blueprint.route('/', methods=['PUT'])
def update_test():
    data = request.get_json(force=True)
    if data.has_key("id"):
        id = data["id"]
        del data["id"]
    else:
        return 10002
    if not (isinstance(data, dict)):
        logger.error("create test, data is not dict: data {}".format(data))

    res = blog_user.update_user(data, id)
    if res:
        return jsonify({"code": 0})
    return jsonify({"code": 10001})


@blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json(force=True)
    username = data["username"]
    password = data["password"]
    if not (isinstance(data, dict)):
        logger.error("create test, data is not dict: data {}".format(data))

    res = blog_user.get_one({"username": username})
    if res and res[0]["password"] == password:
        return jsonify({"code": 0, "token": res[0]["id"], "username": username})
    return jsonify({"code": 10002, "message": "用户名或密码错误"})
