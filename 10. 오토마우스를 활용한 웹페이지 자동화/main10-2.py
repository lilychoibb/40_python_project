# 네이버에서 자동으로 김포 날씨 검색하는 코드

import pyautogui
import time
import pyperclip

# 창을 반으로 나누었을 때의 네이버 검색창 좌표
pyautogui.moveTo(1087, 208, 0.2)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("김포 날씨")
pyautogui.hotkey("command", "v")
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)

# 날씨 화면 자동 캡처 후 저장
start_x = 758
start_y = 258
end_x = 1411
end_y = 661

screenshot = pyautogui.screenshot(region=(start_x, start_y, end_x-start_x, end_y-start_y))
screenshot.save('/Users/lily/workspace/40_python_proj/10. 오토마우스를 활용한 웹페이지 자동화/김포날씨.png')