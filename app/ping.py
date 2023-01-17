from os import popen
from platform import system
from random import shuffle
from time import sleep

from datetime import datetime
from datas import data_read_from_file, data_write_file
from check_packet_loss import read_from_console
from main import start


def ping() -> None:
    try:
        while True:
            file = data_read_from_file()
            shuffle(file)
            op_system = system()
            ping_command = "ping -n 5 " if op_system == "Windows" else "ping -c 5 "
            time_before = datetime.now()
            print("\n")
            print("SCAN IP START ON " + str(time_before))

            for ip in file:
                command = ping_command + ip["ip_address"]
                response = popen(command)
                response_answer = response.readlines()
                percent_loss = read_from_console(response_answer)
                if percent_loss == 100:
                    ip["status"] = "OFF"
                elif percent_loss >= 99:
                    ip["status"] = "NEED CHECK"
                    print(ip)
                else:
                    ip["status"] = "ON"

            time_after = datetime.now()
            total = time_after - time_before
            print("SCAN IP COMPLETED IN: ", total)
            data_write_file(file)
            sleep(300)
    except KeyboardInterrupt:
        print("\n")
        print("SCANNING IS STOP!")
        exit()
    finally:
        start()