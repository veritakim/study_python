'''
    numbers라는 빈 리스트를 만들고 리스트를 출력한다.
    append를 이용해서 numbers에 1, 7, 3, 6, 5, 2, 13, 14를 순서대로 추가한다. 그 후 리스트를 출력한다.
    numbers 리스트의 원소들 중 홀수는 모두 제거한다. 그 후 다시 리스트를 출력한다.
    numbers 리스트의 인덱스 0 자리에 20이라는 수를 삽입한 후 출력한다.
    numbers 리스트를 정렬한 후 출력한다.
    실행 결과
'''

# 빈 리스트 만들기
numbers = []
print(numbers)

# numbers에 값들 추가
# 코드를 입력하세요
numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)
print(numbers)


# numbers에서 홀수 제거
# 코드를 입력하세요
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 1:
        print(numbers[i])
        del numbers[i]
        i -= 1
    else:
        i += 1


# numbers의 인덱스 0 자리에 20이라는 값 삽입
# 코드를 입력하세요
numbers.insert(0, 20)
print(numbers)

# numbers를 정렬해서 출력
# 코드를 입력하세요
numbers.sort()
print(numbers)


''' 
 리스트 꿀 팁
 어떤 값이 리스트에 있는지 확인하는 함수
'''

# value가 some_list의 요소인지 확인
def in_list(some_list, value):
    i = 0
    while i < len(some_list):
        # some_list에서 value를 찾으면 True를 리턴
        if some_list[i] == value:
            return True
        i = i + 1

    # 만약 some_list에서 value를 발견하지 못했으면 False를 리턴
    return False

# 테스트
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(in_list(primes, 7))
print(in_list(primes, 12))


# 파이썬에 함수가 이미 내장되어 있다
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 in primes)
print(12 in primes)


# 거꾸로 값이 없는지 확인하려면
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 not in primes)
print(12 not in primes)


# 리스트 안의 리스트 (Nasted List)
# 세 번의 시험을 보는 수업
grades = [[62, 75, 77], [78, 81, 86], [85, 91, 89]]

# 첫 번째 학생의 성적
print(grades[0])

# 세 번째 학생의 성적
print(grades[2])

# 첫 번째 학생의 첫 번째 시험 성적
print(grades[0][0])

# 세 번째 학생의 두 번째 시험 성적
print(grades[2][1])

# 첫 번째 시험의 평균
print((grades[0][0] + grades[1][0] + grades[2][0]) / 3)



# 리스트의 정렬
numbers = [5, 3, 7, 1]
numbers.sort()
print(numbers)
# 역순으로 하고 싶다면 .reverse()
numbers.reverse()
print(numbers)



# .index("찾고싶은 문장") 리스트에서 찾고 싶은 스트링값의 리스트 인덱스 번호를 알려준다
members = ["영훈", "윤수", "태호", "혜린"]
print(members.index("윤수"))
print(members.index("태호"))


# .remove(x) 리스트에서 x를 삭제해준다
fruits = ["딸기", "당근", "파인애플", "수박", "참외", "메론"]
fruits.remove("파인애플")
print(fruits) # ['딸기', '당근', '수박', '참외', '메론']