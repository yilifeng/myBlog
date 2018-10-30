from flask import Flask
from werkzeug.utils import find_modules, import_string

def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app

def register_blueprints(app):
    for name in find_modules("app.handler"):
        mod = import_string(name)
        if hasattr(mod, "blueprint"):
            app.register_blueprint(mod.blueprint)
    return None


if __name__ == '__main__':
    app = create_app()
    app.run()
