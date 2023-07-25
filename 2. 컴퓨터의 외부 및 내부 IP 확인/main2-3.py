# 컴퓨터의 외부 IP를 알아보기

import requests
import re

req = requests.get("http://ipconfig.kr")
# print(req.text)
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]

print(out_addr)