#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import random
import time


# Создаем TCP/IP сокет
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Привязываем сокет к порту
server_address = ('127.0.0.1', 20001)
print('Старт сервера на {} порт {}'.format(*server_address))
sock.bind(server_address)

# Задаем размер буферной памяти
bufferSize = 1024

print("Термометр работает")


def temperature():
    return str(random.randint(-5, 24))


while True:
    bytesAddressPair = sock.recvfrom(bufferSize)
    message = bytesAddressPair[0].decode("utf-8")
    address = bytesAddressPair[1]
    print("Статус:{}".format(message))
    print("Данные клиента:{}".format(address))
    while True:
        time.sleep(1)
        current_temp = temperature()
        print("Показания термометра - " + current_temp)
        sock.sendto(current_temp.encode("utf-8"), address)
