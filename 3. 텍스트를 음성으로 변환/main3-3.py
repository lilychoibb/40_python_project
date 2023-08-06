# 텍스트 파일에서 문자를 읽어 음성으로 출력

import os
from gtts import gTTS
from playsound import playsound

os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = '대본.txt'

with open(file_path, 'rt', encoding='UTF8') as f:
    read_file=f.read()

tts = gTTS(read_file, lang='ko')
tts.save('대본읽기.mp3')

playsound('대본읽기.mp3')