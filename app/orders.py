import os

from typing import Any
from sys import exit
from time import sleep
from datas import data_read_from_file, data_write_file
from pythonping import ping
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
            os.system("cls")
            print_info()
            work = False
        elif read == "ping":
            call_ping()
        elif read == "stop":
            exit()
        else:
            print("\nWrite CORRECT command and try again!")
            write_command()


def call_ping() -> Any:
    counter = 0
    try:
        while True:
            file = data_read_from_file()
            for user in file:
                address = user["ip_address"]
                ping_test = ping(address)
                ping_result = ping_test.packet_loss
                user["status"] = "ON" if not ping_result else "OFF"
            data_write_file(file)
            os.system("cls")
            print(f"Minutes passed: {counter}")
            print_info()
            sleep(60)
            counter += 1

    except KeyboardInterrupt:
        print("\n")
        print("SCANNING STOP!")
        write_command()


def add_info() -> Any:
    try:
        load_info = data_read_from_file()
        added_data = [dict()]
        added_data[0]["name"] = input("Enter name PC: ")
        added_data[0]["ip_address"] = input("Enter IP address: ")
        added_data[0]["status"] = None
        load_info += added_data
        data_write_file(load_info)
        print("ADD info successful!")
    except KeyboardInterrupt:
        print("\n")
        print("'add' operation was canceled")
        sleep(2)
        os.system("cls")
        write_command()


def upd_info(address: str) -> Any:
    load_info = data_read_from_file()
    try:
        for user in load_info:
            if user["ip_address"] == address:

                while True:
                    chose = input("\nWhat you want to change, ip/name/stop: ")
                    if chose == "ip":
                        new_ip = input("\nEnter new ip_address: ")
                        if new_ip == address or len(new_ip) < 8:
                            while True:
                                print("\nNew ip_address is not correct, please check data and try again!")
                                new_ip = input("\nEnter CORRECT ip_address: ")
                                if new_ip != address and len(new_ip) > 8:
                                    break
                        user["ip_address"] = new_ip
                        print("\nupgrade 'ip_address' was successful!")
                        break
                    elif chose == "name":
                        user[chose] = input("\nEnter new name: ")
                        print("\nupgrade 'name' was successful!")
                        break
                    elif chose == "stop":
                        print("\n'upd' was stopped")
                        break
                    else:
                        print("Incorrect attribute-name")
                data_write_file(load_info)
                break
            else:
                print(f"\nAfter check {address} is not found!")
    except KeyboardInterrupt:
        print("\n")
        print("'upd' operation was canceled")
        sleep(2)
        os.system("cls")
        write_command()


def del_info(ip_address: str) -> Any:
    try:
        load_info = data_read_from_file()
        for user in load_info:
            if user["ip_address"] == ip_address:
                dict_index = load_info.index(user)
                load_info.pop(dict_index)
                data_write_file(load_info)
                print("\nDelete was successful!")
                break
            print(f"\nAfter check {ip_address} is not found!")
    except KeyboardInterrupt:
        print("\n")
        print("'del' operation was canceled")
        sleep(2)
        os.system("cls")
        write_command()


def print_info() -> Any:
    for _ in range(1):
        for line_upd in data_read_from_file():
            print("\n")
            print(line_upd, end="\n")


def write_command() -> None:
    try:
        while True:
            print("\n")
            check_command(input("Chose command: add/upd/del/print/ping/stop \n"))
    except KeyboardInterrupt:
        print("\n")
        print("Program has STOP by user!")


if __name__ == '__main__':
    write_command()
