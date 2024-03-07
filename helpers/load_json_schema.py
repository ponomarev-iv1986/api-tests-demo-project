import json
import os.path

from config import BASE_DIR


def load_schema(file_name):
    path = os.path.join(
        BASE_DIR, 'resources', 'project_resources', 'json_schemas', file_name
    )
    with open(path, encoding='utf-8') as file:
        return json.loads(file.read())
