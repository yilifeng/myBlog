#!/usr/bin/env python
# coding:utf-8


class APIBaseException(Exception):
    status_code = 9999
    message = "Server Exception"

    def __init__(self, message=None, status_code=None, payload=None):
        Exception.__init__(self)
        if message is not None:
            if self.message:
                self.message = "{}: {}".format(self.message, message)
            else:
                self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        if self.status_code is not None:
            rv['status'] = self.status_code
        rv['error_info'] = self.message
        return rv


# 这是一个没有message的错误码，由调用的地方传入message
class ObjectNoMSGException(APIBaseException):
    status_code = 10000
    message = ""