#!/usr/bin/env python
# coding:utf-8

from flask import Blueprint
from ..common import log
from ..model import test
from flask import jsonify

logger = log.get_logger()

blueprint = Blueprint("admin", __name__, url_prefix="/test")


@blueprint.route('/', methods=['GET'])
def hello_world():
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
