from datas import data_read_from_file, data_write_file
from typing import Any
from main import ping
from sys import exit

work = True


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
        elif read == "print":
            print_info()
        elif read == "ping":
            start_ping()
        elif read == "stop":
            exit()


def start_ping() -> Any:
    try:
        ping()
    except IndexError:
        print("\nError, stop scanning")
        exit()


def add_info() -> Any:
    load_info = data_read_from_file()
    added_data = [dict()]
    added_data[0]["name"] = input("Enter name PC: ")
    added_data[0]["ip_address"] = input("Enter IP address: ")
    load_info += added_data
    data_write_file(load_info)
    print("ADD info successful!")


def upd_info(ip_address: str) -> Any:
    load_info = data_read_from_file()
    for user in load_info:
        if user["ip_address"] == ip_address:

            while True:
                chose = input("\nip_address/name/stop ")
                if chose == "ip_address":
                    user[chose] = input("\nEnter new ip_address: ")
                    print("\nDelete was successful!")
                    break
                elif chose == "name":
                    user[chose] = input("\nEnter new name: ")
                    print("\nDelete was successful!")
                    break
                elif chose == "stop":
                    print("\nMode 'upd' was stopped")
                    break
                else:
                    print("Incorrect attribute-name")
            data_write_file(load_info)
            break
        print(f"\nAfter check {ip_address} is not found!")


def del_info(ip_address: str) -> Any:
    load_info = data_read_from_file()
    for user in load_info:
        if user["ip_address"] == ip_address:
            dict_index = load_info.index(user)
            load_info.pop(dict_index)
            data_write_file(load_info)
            print("\nDelete was successful!")
            break
    print(f"\nAfter check {ip_address} is not found!")


def print_info() -> Any:
    for line_upd in data_read_from_file():
        print("\n")
        print(line_upd, end="\n")
    exit()


if __name__ == '__main__':
    try:
        while True:
            print("\n")
            info_from_terminal = check_command(input("Chose command: add/upd/del/print/ping \n"))
    except KeyboardInterrupt:
        print("\n")
        print("Program has STOP by user!")
