from flask import Flask
from .files.routes import example_route
from .config import UPLOAD_FOLDER


def create_app():
    app = Flask(__name__)
    app.register_blueprint(example_route, url_prefix='/files')
    app.config['MAX_CONTENT_LENGTH'] = 42 * 1024 * 1024
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    return app
