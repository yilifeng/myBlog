#!/usr/bin/env python
# coding:utf-8

from . import get_db_conn
from ..common import log
import traceback
from . import dict_2_str_update
from . import get_uuid_id
import common
from blog_article import create_article
from blog_mainkey import create_mainkey
from blog_discuss import create_discuss
from blog_count import create_count

logger = log.get_logger()


def get_one(param):
    return common.get_data("db_blog_content", param)


def delete_one(param):
    return common.delete_one("db_blog_content", param)


def create_content(param):
    try:
        logger.debug(param)
        conn = get_db_conn()
        cursor = conn.cursor()
        res = True
        content_id = get_uuid_id()

        sql = "INSERT INTO db_blog_content(id, content) VALUES(?, ?)"
        cursor.execute(sql, (content_id, param["content"]))
        conn.commit()
        cursor.close()
        param["articleId"] = get_uuid_id()
        param["contentId"] = content_id
        param["categoryId"] = get_uuid_id()
        param["mainkeyId"] = get_uuid_id()
        param["discussId"] = get_uuid_id()
        res &= create_article(param)
        res &= create_count(param)
        return res
    except:
        logger.debug(traceback.format_exc())
        return False


def update_content(param, id):
    try:
        logger.debug(param)
        conn = get_db_conn()
        cursor = conn.cursor()

        data = dict_2_str_update(param)
        sql = "UPDATE db_blog_content SET {} WHERE id=?".format(','.join(data[0]))
        data[1].append(id)
        cursor.execute(sql, tuple(data[1]))
        conn.commit()
        cursor.close()
        return True
    except:
        logger.debug(traceback.format_exc())
        return False
