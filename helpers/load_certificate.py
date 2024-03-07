import os.path

from config import BASE_DIR


def load_cert(file_name):
    return os.path.join(BASE_DIR, 'resources', 'project_resources', 'certs', file_name)
