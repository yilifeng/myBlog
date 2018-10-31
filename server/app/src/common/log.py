#!/usr/bin/env python
# coding:utf-8

import os
import logging
from logging.handlers import RotatingFileHandler

def __get_log_file_path():
    return os.path.join("../logs", 'blog.log')


__LOG_FILE_PATH = __get_log_file_path()

__log_format = "%(asctime)s %(levelname)s [%(filename)s:%(lineno)d]: %(message)s"
log_handler = RotatingFileHandler(__LOG_FILE_PATH, mode="a", maxBytes=1024 * 1024 * 10, backupCount=5)
log_handler.setFormatter(logging.Formatter(__log_format))

__logger = logging.getLogger("blog")
__logger.addHandler(log_handler)
__logger.setLevel(eval("logging.DEBUG"))


def get_logger(name=None, level=logging.DEBUG):
    return __logger
