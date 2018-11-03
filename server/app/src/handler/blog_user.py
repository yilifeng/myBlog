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
    data = blog_user.get_one(id)
    logger.debug("get test info: {}".format(data[0]["content"]))
    return jsonify({"status": 0, "data": data[0]["content"]})


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
