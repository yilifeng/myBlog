#!/usr/bin/env python
# coding:utf-8

from . import get_db_conn

def db_get_test_data():
    conn = get_db_conn()
    cursor = conn.cursor()

    query = "SELECT id, username, password, create_time, update_time FROM t_test_info"
    rs = cursor.execute(query)
    data = rs.fetchall()
    cursor.close()
    return data