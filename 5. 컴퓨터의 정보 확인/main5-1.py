# 컴퓨터의 정보 확인

import psutil

# cpu의 속도 출력
cpu = psutil.cpu_freq()
print(cpu)

# cpu의 물리코어 수 출력
cpu_core = psutil.cpu_count(logical=False)
print(cpu_core)

# 메모리의 정보 출력
memory = psutil.virtual_memory()
print(memory)

# 디스크 정보 출력
disk = psutil.disk_partitions()
print(disk)

# 네트워크를 통해 보내고 받은 데이터량 출력
net = psutil.net_io_counters()
print(net)