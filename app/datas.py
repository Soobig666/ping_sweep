import json
import os
import sys


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


def data_read_from_file() -> list:
    with open(resource_path("users.json"), "r") as opened_file:
        from_file = json.load(opened_file)
        opened_file.close()
    return from_file


def data_write_file(info: (list, dict)) -> None:
    if isinstance(info, list):
        with open(resource_path("users.json"), "w") as opened_file:
            json.dump(info, opened_file)
            opened_file.close()
    else:
        load_data = data_read_from_file()
        load_data += info
        with open(resource_path("users.json"), "w") as opened_file:
            json.dump(load_data, opened_file)
            opened_file.close()
