# 다수의 쓰레드를 동작시키는 코드

import threading

def sum(name, value):
    for i in range(0, value):
        print(f"{name} : {i}")

# 하나의 함수에 입력값을 변경하여 여러개의 쓰레드를 동작시킴
t1 = threading.Thread(target=sum, args=('1번 쓰레드', 10))
t2 = threading.Thread(target=sum, args=('2번 쓰레드', 10))

t1.start()
t2.start()

print("Main Thread")