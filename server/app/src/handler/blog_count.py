#!/usr/bin/env python
# coding:utf-8

from flask import Blueprint
from ..common import log
from ..model import blog_count
from flask import jsonify
from flask import request

logger = log.get_logger()

blueprint = Blueprint("count", __name__, url_prefix="/count")


@blueprint.route('/<id>', methods=['GET'])
def get_one(id):
    data = blog_count.get_one(id)
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

    res = blog_count.create_count(data)
    if res:
        return jsonify({"code": 0})
    return jsonify({"code": 10001})


@blueprint.route('/', methods=['DELETE'])
def delete_test():
    data = request.get_json(force=True)
    if not (isinstance(data, dict)):
        logger.error("create test, data is not dict: data {}".format(data))

    res = blog_count.delete_one(data)
    if res:
        return jsonify({"code": 0})
    return jsonify({"code": 10001})


@blueprint.route('/<id>', methods=['DELETE'])
def delete_one_test(id):
    res = blog_count.delete_one({"id": id})
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

    res = blog_count.update_count(data, id)
    if res:
        return jsonify({"code": 0})
    return jsonify({"code": 10001})
