# 파일에서 문자를 읽어 줄별로 한글로 번역하는 코드

import googletrans

translator = googletrans.Translator()

read_file_path = r"/Users/lily/workspace/40_python_proj/9. 영어로된 문서를 한글로 자동번역/English sentence.txt"
write_file_path = r"/Users/lily/workspace/40_python_proj/9. 영어로된 문서를 한글로 자동번역/Korean.txt"

with open(read_file_path, 'r') as f:
    readLines = f.readlines()

for lines in readLines:
    result1 = translator.translate(lines, dest='ko')
    print(result1.text)
    # 번역 내용을 새 파일로 저장
    with open(write_file_path, 'a', encoding='UTF8') as f:
        f.write(result1.text + '\n')