from datas import data_read_from_file, data_write_file
from typing import Any


work = True


def question() -> Any:
    global work


def check_command(read: str) -> Any:
    global work
    work = True
    while work:

        if read == "upd":
            upd_info(input("Enter IP to change: "))
            work = False
        elif read == "del":
            del_info(input("Enter IP to delete: "))
            work = False
        elif read == "add":
            add_info()
            work = False


def add_info() -> Any:
    load_info = data_read_from_file()
    added_data = [dict()]
    added_data[0]["name"] = input("Enter name PC: ")
    added_data[0]["ip_address"] = input("Enter IP address: ")
    load_info += added_data
    data_write_file(load_info)
    print("ADD info successful!")


def upd_info(command: str) -> Any:
    pass


def del_info(command: str) -> Any:
    pass


def print_info() -> Any:
    for line_upd in data_read_from_file():
        print(line_upd, end="\n")


if __name__ == '__main__':
    try:
        while True:
            print("\n")
            info_from_terminal = check_command(input("Chose command: add/upd/del/print \n"))
    except KeyboardInterrupt:
        print("\n")
        print("Program has STOP by user!")
