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
        logger.debug("param : {}".format(param))
        if param:
            data = dict_2_str_update(param)
            query = "SELECT * FROM {} WHERE {}".format(table, ','.join(data[0]))
            logger.debug("query is : {}".format(query))
            rs = cursor.execute(query, tuple(data[1]))
        else:
            query = "SELECT * FROM {}".format(table)
            rs = cursor.execute(query)
        data = rs.fetchall()
        res = []
        d = {}
        for one_data in data:
            for idx, col in enumerate(cursor.description):
                logger.debug("idx: {}, col: {}".format(idx, col))
                d[col[0]] = one_data[col[0]]
            res.append(d)

        logger.debug("query res: {}".format(res))

        cursor.close()

        return res
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

