import json


# from_file = json.load(opened_file)
# json.dump(from_file, opened_file)

def data_read_from_file() -> dict:
    with open("app/users_dict.json", "r") as opened_file:
        from_file = json.load(opened_file)
    return from_file
