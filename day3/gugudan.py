# while문을 사용해서 구구단 프로그램을 만들어 봅시다.
i = 1
j = 1

while i < 10:
    j = 1 # 중간에 while이 끊겼다. 왜냐하면 j는 9인 상태에서 빠져 나와 중첩 while문이 실행되지 않기 때문이다. 그래서 j를 1로 초기화 시켜줬다.
    while j < 10:
        print(f"{i} * {j} = {i * j}")
        j += 1
    i += 1
