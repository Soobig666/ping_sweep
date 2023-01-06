import json


def data_read_from_file() -> list:
    with open("users.json", "r") as opened_file:
        from_file = json.load(opened_file)
        opened_file.close()
    return from_file


def data_write_file(info: (list, dict)) -> None:
    if isinstance(info, list):
        with open("users.json", "w") as opened_file:
            json.dump(info, opened_file)
            opened_file.close()
    else:
        load_data = data_read_from_file()
        load_data += info
        with open("users.json", "w") as opened_file:
            json.dump(load_data, opened_file)
            opened_file.close()
