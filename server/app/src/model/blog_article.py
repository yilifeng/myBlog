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
    return common.get_data("db_blog_article", param)


def delete_one(param):
    return common.delete_one("db_blog_content", param)


def create_article(param):
    try:
        logger.debug(param)
        conn = get_db_conn()
        cursor = conn.cursor()

        sql = "INSERT INTO db_blog_article(id, contentId, title, abstr, categoryId, hotTag, " \
              "mainKeyId, author, authorId) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, (param["articleId"], param["contentId"], param["title"], param["abstr"], param["categoryId"],
                             0, param["mainkeyId"], param["author"], param["authorId"]))
        conn.commit()
        cursor.close()
        return True
    except:
        logger.debug(traceback.format_exc())
        return False


def update_article(param, id):
    try:
        logger.debug(param)
        conn = get_db_conn()
        cursor = conn.cursor()

        data = dict_2_str_update(param)
        sql = "UPDATE db_blog_article SET {} WHERE id=?".format(','.join(data[0]))
        data[1].append(id)
        cursor.execute(sql, tuple(data[1]))
        conn.commit()
        cursor.close()
        return True
    except:
        logger.debug(traceback.format_exc())
        return False
