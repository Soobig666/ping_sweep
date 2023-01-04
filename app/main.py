import os
import platform

from time import sleep
from datetime import datetime
from work_with_datas import data_read_from_file, data_write_file


# KeyboardInterrupt
while True:
    file = data_read_from_file()

    op_system = platform.system()
    ping_command = "ping -n 2 " if op_system == "Windows" else "ping -c 2 "
    time_before = datetime.now()
    print("Сканирование запущено В: " + str(time_before))

    for ip in file:
        command = ping_command + ip["ip_address"]
        response = os.popen(command)
        flag = False

        for line in response.readlines():
            if "ttl" in line:
                temp_flag = True

        if not flag:
            ip["status"] = "OFF"
        else:
            ip["status"] = "ON"

    time_after = datetime.now()
    total = time_after - time_before
    print("Сканирование окончено за: ", total)
    data_write_file(file)
    sleep(300)
