# qr코드 생성

import qrcode

qr_data = "www.naver.com"
qr_img = qrcode.make(qr_data)

save_qrcode='./' + qr_data + '.png'
qr_img.save(save_qrcode)