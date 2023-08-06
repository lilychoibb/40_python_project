# 텍스트를 음성으로 변환하기

from gtts import gTTS
import socket
import requests
import re

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.com", 443))

# print("내부 IP: ", in_addr.getsockname()[0])

req = requests.get("http://ipconfig.kr")
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]

print("외부 IP: ", out_addr)

text = f"안녕하세용 지금은 카페에요 어지럽네요. 여기 아이피는 {out_addr} 입니다."

tts = gTTS(text=text, lang='ko')
tts.save("./hi2.mp3")
