import os
import json
import uuid
from KeyValueStore.settings import STORAGE_DIR


def get_user_file_name(user_id):
    file_name = STORAGE_DIR + "/" + user_id + ".json"
    if os.path.exists(file_name):
        return file_name
    raise ValueError("Given unknown user id.")


def new_user_identifier():
    uuid_res = str(uuid.uuid4())
    file_name = STORAGE_DIR + "/" + uuid_res + ".json"
    with open(file_name, 'w') as f:
        data = {"key": None, "value": None}
        f.writelines(json.dumps(data))
    return uuid_res
