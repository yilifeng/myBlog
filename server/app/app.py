#!/usr/bin/env python
# coding:utf-8

from flask import Flask
from flask import g
from flask import request as r
from werkzeug.utils import find_modules, import_string
from flask_cors import CORS
import sqlite3
from src.common import log

logger = log.get_logger("app")

def create_app():
    app = Flask(__name__)
    # 处理跨域访问
    CORS(app)
    # 注册URL Handler
    register_blueprints(app)
    reg_before_request(app)
    init_sqlite(app)
    return app


def register_blueprints(app):
    for name in find_modules("src.handler"):
        mod = import_string(name)
        if hasattr(mod, "blueprint"):
            app.register_blueprint(mod.blueprint)
    return None


def init_sqlite(app):
    @app.cli.command("init_db")
    def init_db_command():
        """Creates the database tables."""
        print("Initialized the database.")


def reg_before_request(app):
    @app.before_request
    def before_request():
        app.logger.debug("{} {} {} {}".format(r.remote_addr, r.method, r.path, r.data))
        g.db_conn = connect_db()  # db_pool.connection()
        g.db_conn.row_factory = sqlite3.Row


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect("../doc/database/blog.db3")
    rv.row_factory = sqlite3.Row
    return rv


if __name__ == '__main__':
    app = create_app()
    app.run()
