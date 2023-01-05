import os
import platform

from time import sleep
from datetime import datetime
from work_with_datas import data_read_from_file, data_write_file
from check_packet_loss import read_from_console


def ping() -> None:
    while True:
        file = data_read_from_file()
        op_system = platform.system()
        ping_command = "ping -n 2 " if op_system == "Windows" else "ping -c 2 "
        time_before = datetime.now()
        print("Сканирование запущено в " + str(time_before))

        for ip in file:
            command = ping_command + ip["ip_address"]
            response = os.popen(command)
            percent_loss = read_from_console(response.readlines())
            if percent_loss == 100:
                ip["status"] = "OFF"
            elif percent_loss <= 99:
                ip["status"] = "NEED CHECK"
                print(ip)
            else:
                ip["status"] = "ON"

        time_after = datetime.now()
        total = time_after - time_before
        print("Сканирование окончено за: ", total)
        data_write_file(file)
        sleep(300)


if __name__ == '__main__':
    ping()
