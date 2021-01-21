'''
    numbers라는 리스트가 주어졌습니다.

for문과 range 함수를 사용하여, numbers의 인덱스와 원소를 출력해 보세요.
'''

numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# 인덱스와 원소 출력
# 코드를 입력하세요.
for i in numbers:
    print(numbers.index(i), i)


'''
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# 인덱스와 원소 출력
for i in range(len(numbers)):
    print(i, numbers[i])
'''