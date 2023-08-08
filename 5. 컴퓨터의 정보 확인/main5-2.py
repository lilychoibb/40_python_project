# 필요한 정보만 출력하는 코드

import psutil

cpu = psutil.cpu_freq()
cpu_current_ghz = round(cpu.current / 1000, 2)
# current 함수는 현재 내부 포인터에서 가리키고 있는 배열 원소의 값을 반환
print(f"cpu속도: {cpu_current_ghz}GHz")

cpu_core = psutil.cpu_count(logical=False)
print(f"코어: {cpu_core}개")

memory = psutil.virtual_memory()
memory_total = round(memory.total / 1024**3)
print(f"메모리: {memory_total}GB")

disk = psutil.disk_partitions()
for p in disk:
    print(p.mountpoint, p.fstype, end='')
    # 디스크의 마운트 위치, 파일시스템 타입 출력
    du = psutil.disk_usage(p.mountpoint)
    disk_total = round(du.total / 1024**3)
    print(f" 디스크크기: {disk_total}GB")


net = psutil.net_io_counters()
sent = round(net.bytes_sent / 1024**2, 1)
recv = round(net.bytes_recv / 1024**2, 1)
print(f"보내기 : {sent}MB 받기 : {recv}MB")
# 보내고 받은 데이터는 누적데이터 값
