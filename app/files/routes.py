from flask import Blueprint, send_from_directory, request
from .models import File
from app.config import UPLOAD_FOLDER
example_route = Blueprint('files', __name__)


@example_route.route('/upload', methods=["POST"])
def upload():
    file = File(request.files['file'])
    print(file.file)
    print(file.get_hash())
    file.save(file.get_hash())
    return file.get_hash()



@example_route.route('/download/<name>')
def download_file(name):
    return send_from_directory(UPLOAD_FOLDER, name)