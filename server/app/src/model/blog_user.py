#!/usr/bin/env python
# coding:utf-8

from . import get_db_conn
from ..common import log
import traceback
from . import dict_2_str_update
from . import get_uuid_id
import common

logger = log.get_logger()


def get_one(param=None):
    data = common.get_data("db_blog_user", param)
    res = []
    for one_data in data:
        tmp = {}
        tmp["id"] = one_data["id"]
        tmp["username"] = one_data["username"]
        tmp["password"] = one_data["password"]
        res.append(tmp)
    return res


def delete_one(param):
    return common.delete_one("db_blog_user", param)


def create_user(param):
    try:
        logger.debug(param)
        conn = get_db_conn()
        cursor = conn.cursor()

        sql = "INSERT INTO db_blog_user(id, username, password) VALUES(?, ?, ?)"
        cursor.execute(sql, (get_uuid_id(), param["username"], param["password"]))
        conn.commit()
        cursor.close()
        return True
    except:
        logger.debug(traceback.format_exc())
        return False


def update_user(param, id):
    try:
        logger.debug(param)
        conn = get_db_conn()
        cursor = conn.cursor()

        data = dict_2_str_update(param)
        sql = "UPDATE db_blog_user SET {} WHERE id=?".format(','.join(data[0]))
        data[1].append(id)
        cursor.execute(sql, tuple(data[1]))
        conn.commit()
        cursor.close()
        return True
    except:
        logger.debug(traceback.format_exc())
        return False
