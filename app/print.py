from datas import data_read_from_file
from typing import Any


def check_command(read: str) -> Any:
    pass


def set_info(command: str) -> Any:
    pass


def upd_info(command: str) -> Any:
    pass


def del_info(command: str) -> Any:
    pass


if __name__ == '__main__':
    for line in data_read_from_file():
        print(line, end="\n")

    info_from_terminal = check_command(input("new/upd/del"))
