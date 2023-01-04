import os
import platform

from time import sleep
from datetime import datetime
from work_with_datas import data_read_from_file


# KeyboardInterrupt
while True:
    file = data_read_from_file()
    ip_list = [number["name"] for number in file]
    op_system = platform.system()
    ping_command = "ping -n 2 " if op_system == "Windows" else "ping -c 2 "
    time_before = datetime.now()
    print("Сканирование запущено:")

    for ip in ip_list:
        command = ping_command + ip
        response = os.popen(command)
        temp_flag = False

        for line in response.readlines():
            if "ttl" in line:
                temp_flag = True

        if not temp_flag:
            print(ip, "--> OFF")
        else:
            print(ip, "--> ON")

    time_after = datetime.now()
    total = time_after - time_before
    print("Сканирование окончено за: ", total)
    sleep(300)
