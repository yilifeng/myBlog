from flask import Blueprint

blueprint = Blueprint("admin", __name__, url_prefix="/test")

@blueprint.route('/')
def hello_world():
    print "aaa"
    return 'Hello World!'