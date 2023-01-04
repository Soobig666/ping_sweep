import os
import platform

from time import sleep
from datetime import datetime


while True:
    host = input("Введите адрес сети: ")
    splited_host = host.split('.')
    cleaned_host = splited_host[0] + '.' + splited_host[1] + '.'\
        + splited_host[2] + '.'

    start_ping = int(input("Диапазон сканирования ОТ: "))
    ended_ping = int(input("Диапазон сканирования ДО: ")) + 1
    op_system = platform.system()

    if op_system == "Windows":
        ping_command = "ping -n 2 "
    elif op_system == "Linux":
        ping_command = "ping -c 2 "
    else:
        ping_command = "ping -c 2 "
    time_before = datetime.now()
    print("Сканирование запущено:")

    for ip in range(start_ping, ended_ping):
        addr = cleaned_host + str(ip)
        command = ping_command + addr
        response = os.popen(command)
        temp_flag = False

        for line in response.readlines():
            if "ttl" in line:
                temp_flag = True

        if not temp_flag:
            print(addr, "--> OFF")
        else:
            print(addr, "--> ON")

    time_after = datetime.now()
    total = time_after - time_before
    print("Сканирование окончено за: ", total)
    sleep(300)
