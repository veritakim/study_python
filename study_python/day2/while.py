# while 반복문
'''
while 반복문 구조
while 조건 부분:
    수행 부분분

조건 부분은 불린 값으로 계산
조건 부분이 true면 수행 부분을 계속 하게된다
'''


# 나는 잘생겼다 세 번 출력하기
i = 1
while i <= 3:
    print("나는 잘생겼다!")
    i += 1


# while 반복문을 사용하여 1 이상 100 이하의 짝수를 모두 출력해 보세요.
# 내가 쓴 답
i = 1
while i <= 100:
    if (i % 2 == 0):
        print(i)
    i += 1

# 모범 답
i = 1
while i <= 50:
    print(i * 2)
    i += 1

    

# while문을 사용하여, 100 이상의 자연수 중 가장 작은 23의 배수를 출력해 보세요.
# 내가 쓴 답
def min_number():
    i = 100
    while i >= 100:
        if i % 23 == 0:
            return i
        else:
            i += 1


print(min_number())

# 모법 답
i = 100
while i % 23 != 0:
    i += 1

print(i)