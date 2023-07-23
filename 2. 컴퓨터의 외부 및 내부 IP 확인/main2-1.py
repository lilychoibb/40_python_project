# 컴퓨터의 내부 IP를 알아보기

import socket

in_addr = socket.gethostbyname('localhost')

print(in_addr)
