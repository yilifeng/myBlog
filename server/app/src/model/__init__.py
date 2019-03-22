#!/usr/bin/env python
# coding:utf-8

from flask import g
import sqlite3
import os
import uuid

def connect_db():
    """Connects to the specific database."""
    database_path = os.path.join("../../doc/database", 'blog.db3')
    rv = sqlite3.connect(database_path)
    rv.row_factory = sqlite3.Row
    return rv


def get_db_conn():
    if hasattr(g, 'db_conn'):
        return g.db_conn
    else:
        return connect_db()


def get_uuid_id():
    return str(uuid.uuid4())


def dict_2_str_update(dict_in):
    tmp_list_key = []
    tmp_list_value = []
    for k, v in dict_in.items():
        tmp = "%s=?" % (str(k))
        tmp_list_key.append(tmp)
        tmp_list_value.append(v)
    return [tmp_list_key, tmp_list_value]

