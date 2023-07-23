# 컴퓨터의 내부 IP를 알아보기 - 좀 더 정확하게

import socket

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.com", 443))

print(in_addr.getsockname()[0])