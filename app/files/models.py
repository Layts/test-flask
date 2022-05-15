import hashlib
from app.config import UPLOAD_FOLDER
import os


class File:

    def __init__(self, file_bytes):
        self.file = file_bytes
        self.owner = " "

    def get_hash(self):
        return hashlib.md5(self.file.read()).hexdigest()

    def save(self, filename):
        self.file.save(os.path.join(UPLOAD_FOLDER, filename[:2], filename))

    def delete(self):
        pass
