import json


def data_read_from_file() -> list:
    with open("users.json", "r") as opened_file:
        from_file = json.load(opened_file)
        opened_file.close()
    return from_file


def data_write_file(info: list) -> None:
    with open("users.json", "w") as opened_file:
        json.dump(info, opened_file)
        opened_file.close()
