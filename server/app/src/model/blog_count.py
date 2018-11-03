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
    return common.get_data("db_blog_count", param)


def delete_one(param):
    return common.delete_one("db_blog_count", param)


def create_count(param):
    try:
        logger.debug(param)
        conn = get_db_conn()
        cursor = conn.cursor()

        sql = "INSERT INTO db_blog_count(id, contentId, articleId) VALUES(?, ?, ?)"
        cursor.execute(sql, (get_uuid_id(), param["contentId"], param["articleId"]))
        conn.commit()
        cursor.close()
        return True
    except:
        logger.debug(traceback.format_exc())
        return False


def update_count(param, id):
    try:
        logger.debug(param)
        conn = get_db_conn()
        cursor = conn.cursor()

        data = dict_2_str_update(param)
        sql = "UPDATE db_blog_count SET {} WHERE id=?".format(','.join(data[0]))
        data[1].append(id)
        cursor.execute(sql, tuple(data[1]))
        conn.commit()
        cursor.close()
        return True
    except:
        logger.debug(traceback.format_exc())
        return False
