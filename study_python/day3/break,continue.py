# break
'''
 만약 while문의 조건 부분과 상관 없이 반복문을 빠져나오고 싶다면 break를 사요안다
'''

i = 100

while True:
    # i가 23의 배수면 반복문을 끝낸다
    if i % 23 == 0:
        break
    i += 1
print(i)



# continue
'''
 현재 진행되고 있는 수행 부분을 중단하고 바로 조건 부분을 확인하고 싶으면 continue를 사용한다. 
 약간 skip 이라고 생각하면 쉬울 듯
'''
i = 0

while i < 15:
    i += 1

    # i가 홀수면 print(i) 안하고 바로 조건 부분으로 돌아감
    if i % 2 == 1:
        continue
    print(i)