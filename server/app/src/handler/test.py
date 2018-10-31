#!/usr/bin/env python
# coding:utf-8

from flask import Blueprint
from ..common import log
from ..model import test
from flask import jsonify
from flask import request

logger = log.get_logger()

blueprint = Blueprint("admin", __name__, url_prefix="/test")


@blueprint.route('/', methods=['GET'])
def get_test():
    data = test.db_get_test_data()
    res = []
    for d in data:
        res.append({
            "id": d["id"],
            "username": d["username"],
            "password": d["password"],
            "create_time": d["create_time"],
            "update_time": d["update_time"]
        })
    logger.debug("get test info: {}".format(res))
    return jsonify({"data": res})


@blueprint.route('/', methods=['POST'])
def create_test():
    data = request.get_json(force=True)
    if not (isinstance(data, dict)):
        logger.error("create test, data is not dict: data {}".format(data))

    res = test.db_test_create(data)
    if res:
        return jsonify({"code": 0})
    return jsonify({"code": 10001})


@blueprint.route('/', methods=['DELETE'])
def delete_test():
    data = request.get_json(force=True)
    if not (isinstance(data, dict)):
        logger.error("create test, data is not dict: data {}".format(data))

    res = test.db_test_delete(data)
    if res:
        return jsonify({"code": 0})
    return jsonify({"code": 10001})


@blueprint.route('/<id>', methods=['DELETE'])
def delete_one_test(id):
    res = test.db_test_delete({"id": id})
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

    res = test.db_test_update(data, id)
    if res:
        return jsonify({"code": 0})
    return jsonify({"code": 10001})
