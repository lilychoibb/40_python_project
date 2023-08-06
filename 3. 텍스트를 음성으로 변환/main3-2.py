# 음성변환으로 생성되는 .Mp3 파일을 파이썬에서 바로 실행하는 코드

import os
from gtts import gTTS
from playsound import playsound

os.chdir(os.path.dirname(os.path.abspath(__file__)))

text = "안녕하세요 오늘도 카페입니다. 라이브러리가 주는 워닝을 잘 읽어봅시다..."

tts = gTTS(text=text, lang='ko')
tts.save("hihi.mp3")

playsound("hihi.mp3")