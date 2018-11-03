#!/usr/bin/env python
# coding:utf-8

from flask import Blueprint
from ..common import log
from ..model import blog_discuss
from flask import jsonify
from flask import request

logger = log.get_logger()

blueprint = Blueprint("discuss", __name__, url_prefix="/discuss")


@blueprint.route('/<id>', methods=['GET'])
def get_one(id):
    data = blog_discuss.get_one(id)
    logger.debug("get test info: {}".format(data[0]["content"]))
    return jsonify({"status": 0, "data": data[0]["content"]})


@blueprint.route('/', methods=['POST'])
def create():
    data = request.get_json(force=True)
    if not (isinstance(data, dict)):
        logger.error("create test, data is not dict: data {}".format(data))

    res = blog_discuss.create_discuss(data)
    if res:
        return jsonify({"code": 0})
    return jsonify({"code": 10001})


@blueprint.route('/', methods=['DELETE'])
def delete_test():
    data = request.get_json(force=True)
    if not (isinstance(data, dict)):
        logger.error("create test, data is not dict: data {}".format(data))

    res = blog_discuss.delete_one(data)
    if res:
        return jsonify({"code": 0})
    return jsonify({"code": 10001})


@blueprint.route('/<id>', methods=['DELETE'])
def delete_one_test(id):
    res = blog_discuss.delete_one({"id": id})
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

    res = blog_discuss.update_discuss(data, id)
    if res:
        return jsonify({"code": 0})
    return jsonify({"code": 10001})
