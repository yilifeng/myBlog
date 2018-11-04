#!/usr/bin/env python
# coding:utf-8

from flask import Blueprint
from ..common import log
from ..model import blog_mainkey
from flask import jsonify
from flask import request

logger = log.get_logger()

blueprint = Blueprint("mainkey", __name__, url_prefix="/mainkey")


@blueprint.route('/<id>', methods=['GET'])
def get_one(id):
    data = blog_mainkey.get_one(id)
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

    res = blog_mainkey.create_mainkey(data)
    if res:
        return jsonify({"code": 0})
    return jsonify({"code": 10001})


@blueprint.route('/', methods=['DELETE'])
def delete_test():
    data = request.get_json(force=True)
    if not (isinstance(data, dict)):
        logger.error("create test, data is not dict: data {}".format(data))

    res = blog_mainkey.delete_one(data)
    if res:
        return jsonify({"code": 0})
    return jsonify({"code": 10001})


@blueprint.route('/<id>', methods=['DELETE'])
def delete_one_test(id):
    res = blog_mainkey.delete_one({"id": id})
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

    res = blog_mainkey.update_mainkey(data, id)
    if res:
        return jsonify({"code": 0})
    return jsonify({"code": 10001})
