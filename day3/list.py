'''
 list 변수에 여러 개를 저장하고 싶을 때 사용
'''
numbers = [1, 2, 3, 4, 6]
names = ["마크", "윤오", "영호", "정우"]


# 인덱싱 (indexing) : 리스트에 하나 씩 꺼내기 인덱스의 위치를 통해 꺼내오는 것. 인덱스는 0부터 시작한다
print(names[0])


# 파이썬에느 인덱스 - 값이 있다. -1은 끝의 값
print(numbers[-1]) # 6
print(numbers[-2]) # 4


# 리스트 슬라이싱 list slicing : 리스트 자르기
print(numbers[0:4]) # 1, 2, 3, 4
print(numbers[2:]) # 뒤에 아무것도 쓰지 않는다면 끝까지 [3, 4, 6]


'''
 리스트에서 사용할 수 있는 함수
'''
banks = [1, 2]

# len(banks) 리스트의 값이 몇 개 있는지 보여준다
print(len(banks))

# .append() 리스트에 추가하기. 가장 오른쪽 끝에 추가가 된다.
banks.append(5)
print(banks) # [1, 2, 5]

# del 리스트이름[인덱스]
del banks[0]
print(banks) # [2, 5]

# 리스트이름.insert(인덱스, 원하는 숫자) 원하는 인덱스 자리에 값 추가하기
banks.insert(0, 32)
print(banks) # [32, 2, 5]


'''
 리스트 정렬하기
'''
num_2 = [2, 32, 14, 8, 3]

# sorted(리스트이름)  sorted 함수 사용하기
# sorted(리스트이름, revers=True) 반대로 정렬
new_list1 = sorted(num_2)
new_list2 = sorted(num_2, reverse=True)
print(new_list1)
print(new_list2)


# sort 리스트이름.sort
num_3 = [2, 32, 14, 8, 3]
num_3.sort() # 그냥 프린트 하면 none이 나온다. sort는 정렬을 시켜주는 프로그램
print(num_3)


'''
 sorted 와 sort의 차이
 
 sorted : 기존 리스트는 건들이지 않고, 정렬된 새로운 리스트를 리턴
 sort : 아무것도 리턴하지 않고, 기존의 리스트를 정렬시킴
'''

