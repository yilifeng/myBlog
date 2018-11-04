#!/usr/bin/env python
# coding:utf-8

from . import get_db_conn
from ..common import log
import traceback
from . import dict_2_str_update

logger = log.get_logger()


def get_data(table, param=None):
    try:
        conn = get_db_conn()
        cursor = conn.cursor()

        if param:
            data = dict_2_str_update(param)
            query = "SELECT * FROM {} WHERE {}".format(table, ','.join(data[0]))
            rs = cursor.execute(query, tuple(data[1]))
        else:
            query = "SELECT * FROM {}".format(table)
            rs = cursor.execute(query)
        data = rs.fetchall()
        cursor.close()
        return data
    except:
        logger.debug(traceback.format_exc())
        return False


def delete_one(table, param):
    try:
        logger.debug(param)
        conn = get_db_conn()
        cursor = conn.cursor()

        data = dict_2_str_update(param)
        sql = "DELETE FROM {} WHERE {}".format(table, ','.join(data[0]))
        cursor.execute(sql, tuple(data[1]))
        conn.commit()
        cursor.close()
        return True
    except:
        logger.debug(traceback.format_exc())
        return False

