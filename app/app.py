from flask import Flask
from .api.routes import example_route


def create_app():
    app = Flask(__name__)
    app.register_blueprint(example_route, url_prefix='/api')
    return app
