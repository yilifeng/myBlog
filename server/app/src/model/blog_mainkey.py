#!/usr/bin/env python
# coding:utf-8

from . import get_db_conn
from ..common import log
import traceback
from . import dict_2_str_update
from . import get_uuid_id
import common

logger = log.get_logger()


def get_one(param):
    return common.get_data("db_blog_mainkey", param)


def delete_one(param):
    return common.delete_one("db_blog_mainkey", param)


def create_mainkey(param):
    try:
        logger.debug(param)
        conn = get_db_conn()
        cursor = conn.cursor()

        sql = "INSERT INTO db_blog_mainkey(id, contentId, articleId, mainKey) VALUES(?, ?, ?)"
        cursor.execute(sql, (param["mainkeyId"], param["contentId"], param["articleId"], param["mainKey"]))
        conn.commit()
        cursor.close()
        return True
    except:
        logger.debug(traceback.format_exc())
        return False


def update_mainkey(param, id):
    try:
        logger.debug(param)
        conn = get_db_conn()
        cursor = conn.cursor()

        data = dict_2_str_update(param)
        sql = "UPDATE db_blog_mainkey SET {} WHERE id=?".format(','.join(data[0]))
        data[1].append(id)
        cursor.execute(sql, tuple(data[1]))
        conn.commit()
        cursor.close()
        return True
    except:
        logger.debug(traceback.format_exc())
        return False
