# 마우스의 좌표를 출력하는 코드

import pyautogui
import time

while True:
    print(pyautogui.position())
    time.sleep(0.1)