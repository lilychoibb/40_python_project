# 여러개의 QR코드를 한번에 생성하는 코드

import qrcode

file_path = '/Users/lily/workspace/40_python_proj/4. QR코드 생성기/qr코드모음.txt'

with open(file_path, 'rt', encoding='UTF8') as f:
    read_lines = f.readlines()


for line in read_lines:
    line = line.strip()
    print(line)

    qr_data = line
    qr_img = qrcode.make(qr_data)

    save_qrcode = '/Users/lily/workspace/40_python_proj/4. QR코드 생성기/' + qr_data + '.png'
    qr_img.save(save_qrcode)