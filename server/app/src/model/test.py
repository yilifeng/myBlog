#!/usr/bin/env python
# coding:utf-8

from . import get_db_conn
from ..common import log
import traceback

logger = log.get_logger()

def db_get_test_data():
    conn = get_db_conn()
    cursor = conn.cursor()

    query = "SELECT id, username, password, create_time, update_time FROM t_test_info"
    rs = cursor.execute(query)
    data = rs.fetchall()
    cursor.close()
    return data


def db_test_create(param):
    try:
        logger.debug(param)
        conn = get_db_conn()
        cursor = conn.cursor()

        sql = "INSERT INTO t_test_info(username, password) VALUES(?, ?)"
        cursor.execute(sql, (param["username"], param["password"]))
        conn.commit()
        cursor.close()
        return True
    except:
        logger.debug(traceback.format_exc())
        return False


def db_test_delete(param):
    try:
        logger.debug(param)
        conn = get_db_conn()
        cursor = conn.cursor()

        sql = "DELETE FROM t_test_info WHERE username=?"
        cursor.execute(sql, (param["username"],))
        conn.commit()
        cursor.close()
        return True
    except:
        logger.debug(traceback.format_exc())
        return False
