import json

# from_file = json.load(opened_file)
# json.dump(from_file, opened_file)


def data_read_from_file() -> list:
    with open("users_dict.json", "r") as opened_file:
        from_file = json.load(opened_file)
        opened_file.close()
    return from_file


def data_write_file(info: list) -> None:
    with open("users_dict.json", "w") as opened_file:
        json.dump(info, opened_file)
        opened_file.close()
