'''
세트 : 집합을 표현한다. 합집합, 교집합, 차집합을 사용할 수 있다.
'''
# 세트 만들기
a = {"apple", "banana", "orange"}
print(type(a))


# 세트는 리스트 튜플 딕셔너리와 달리 []대괄호로 특정 요소만 출력할 수 없다
# print(a[0]) # 리스트 딕셔너리 튜플은 apple을 기대하지만 error가 난다

# 세트의 특정값이 있는지 확인하기. 있으면 True 없으면 False
print("peach" in a)
print("orange" not in a) # a에 오렌지가 있으니 false를 반환

# 세트 만들기
c = {} # 대괄호 안에 빈공간이면 이건 그냥 딕셔너리다
c = set()
print(type(c))

# 세트는 리스트나 딕셔너리 튜플과 같이 세트 안에 세트는 넣지 못한다
# b = {{1,2}, {3,4}}
# print(b) error

# 프로즌세트 : 내용을 변경할 수 없는 세트
# 변수 = frozenset(반복가능한 객체)
d = frozenset(range(10))
# 중첩사용이 가능하다
e = frozenset({frozenset({1, 2}), frozenset({3, 4})})
print(e)




# 집합 연산사용하기
# | , set.union 합집합
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)
c = set.union(a,b)
print(c)

# 교집합 사용하기
# & , set.intersection
print(a & b)
print(set.intersection(a,b))

# 차집합 사용하기
# - , set.difference
print(a - b)
print(set.difference(a,b))

# 대칭 차집합 : 겹치지 않은 것들만 보여주세요
# ^, set.symmetric_difference
print(a ^ b)
print(set.symmetric_difference(a, b))


# 할당 연산자
# |, &, -, ^ 연산자와 할당 연사자 =을 함께 사용하면 집합 여난의 결과를 변수에 다시 할당한다
# | : 현재 세트에 다른 세트를 더하는 update 메서드와 같음
a |= {5}
print(a) # {1, 2, 3, 4, 5}
a.update({5})
print(a)


# &= 현재 세트와 다른 셑트 중에서 겹치는 요소 intersection_update와 같음
a &= {0, 1, 2, 3}
print(a)
a.intersection_update({0, 1, 2, 3})
print(a)

# -= 현재 세트에서 다른 세트를 빼며 difference_update
a = {1, 2, 3, 4}
a -= {3}
print(a)
a.difference_update({3}, {4})
print(a)

# ^= 현재 세트와 다른 세트 중에서 겹치지 않는 요소만 현재 세트에 저장. symmetric_difference_update
a = {1, 2, 3, 4}
a ^= {3, 4, 5, 6}
print(a)

# 부분 집합과 상위 집합 확인하기
# 부분집합, 진부분집합, 상위집합, 진상위집합과 같이 속하는 관계를 표현

# <= 현재 세트가 다른 세트의 부분집합인지 확인 issubset
b = {1, 3, 5, 7, 9}
print(b <= {1, 3, 5, 7, 9})

# < 현재 세트가 다른 세트의 진 부분집합인지 확인
print(b < {1, 3, 5, 7, 9, 11})


# >= 현재 세트가 다른 세트의 상위집합인지 확인 issuperset
print(b >= {1, 3, 5, 7})

# > 진상위집합

# == 서로 같은지 확인
# != 서로 다른지 확인
print(b == {1, 3, 5, 7, 9})

# disjoint 현재 세트가 다른 세트와 겹치는지 확인하기


