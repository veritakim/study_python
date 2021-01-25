# 파일을 읽는 방법
# with open('파일이름.확장자', 'r') as f:    r은 read 의 약자
# with open('data/sell.txt', 'r') as f:  같은 폴더 안에 있어서 그냥 이름과 확장자만 써도 된다.
with open('data/sell.txt', 'r', encoding='UTF-8') as f:  # sell.txt의 경로를 바꿔주니 자동으로 data/sell.txt로 변경됐다.
    print(type(f)) # <class '_io.TextIOWrapper'>
    for line in f:
        print(line)