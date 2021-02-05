with open('hello2.txt', 'w') as f:
    for i in range(3):
        f.write(f'Hello world! {i} \n')



# 리스트에 들어있는 문자열을 파일에 쓰기
lines = ['안녕하세요\n', '파이썬입니다\n', '쉽지않습니다\n']

with open('hello.txt', 'w', encoding="UTF-8") as f:
    f.writelines(lines)