# 2가지 동작이 동시에 실행되는 코드

import threading
import time

def thread_1():
    while True:
        print("쓰레드1 동작")
        time.sleep(1.0)

t1 = threading.Thread(target=thread_1)
# 쓰레드를 데몬쓰레드로 설정하여 메인동작이 실행될 때만 쓰레드를 실행하도록 함
t1.daemon = True
t1.start()

while True:
    print("메인동작")
    time.sleep(2.0)