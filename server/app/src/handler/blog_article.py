#!/usr/bin/env python
# coding:utf-8

from flask import Blueprint
from ..common import log
from ..model import blog_article
from flask import jsonify
from flask import request

logger = log.get_logger()

blueprint = Blueprint("article", __name__, url_prefix="/article")


@blueprint.route('/<id>', methods=['GET'])
def get_one(id):
    data = blog_article.get_one(id)
    if data:
        logger.debug("get test info: {}".format(data))
        return jsonify({"status": 0, "data": data})
    else:
        return jsonify({"status": 0, "data": []})


@blueprint.route('/', methods=['GET'])
def get_all():
    logger.debug("in get article ...")
    data = blog_article.get_one()
    if data:
        logger.debug("get test info: {}".format(data))
        res = []
        for one in data:
            one_dict = {}
            one_dict["id"] = one["id"]
            one_dict["contentId"] = one["contentId"]
            one_dict["title"] = one["title"]
            one_dict["abstr"] = one["abstr"]
            one_dict["createTime"] = one["createTime"]
            one_dict["updateTime"] = one["updateTime"]
            one_dict["categoryId"] = one["categoryId"]
            one_dict["hotTag"] = one["hotTag"]
            one_dict["mainKeyId"] = one["mainKeyId"]
            one_dict["author"] = one["author"]
            one_dict["authorId"] = one["authorId"]
            res.append(one_dict)
        return jsonify({"status": 0, "data": res})
    else:
        return jsonify({"status": 0, "data": []})


@blueprint.route('/', methods=['POST'])
def create():
    data = request.get_json(force=True)
    if not (isinstance(data, dict)):
        logger.error("create test, data is not dict: data {}".format(data))

    res = blog_article.create_article(data)
    if res:
        return jsonify({"code": 0})
    return jsonify({"code": 10001})


@blueprint.route('/', methods=['DELETE'])
def delete_test():
    data = request.get_json(force=True)
    if not (isinstance(data, dict)):
        logger.error("create test, data is not dict: data {}".format(data))

    res = blog_article.delete_one(data)
    if res:
        return jsonify({"code": 0})
    return jsonify({"code": 10001})


@blueprint.route('/<id>', methods=['DELETE'])
def delete_one_test(id):
    res = blog_article.delete_one({"id": id})
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

    res = blog_article.update_article(data, id)
    if res:
        return jsonify({"code": 0})
    return jsonify({"code": 10001})
