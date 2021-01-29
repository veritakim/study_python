'''
 람다 표현식 사용하기
 - 람다 표현식은 식 형태로 되어있다.
 - 함수를 간편하게 작성할 수 있다
'''

def plus_ten(x):
    return x + 10


print(plus_ten(1))
# >> 11

# plus_ten 함수를 람다 표현식을 작성해보자
# lamda 매개변수들: 식
# 그냥 사용한다면 부르는 함수가 없기때문에 변수에 할당해준다
# 변수이름 = lambda 매개변수: 식

ten_plus = lambda x: x + 10
print(ten_plus(1))
# >> 11


# 매개변수를 할당하지 않고 바로 사용하기
# (lambda 매개변수: 식)(인수 매개변수에 들어갈 수)
print((lambda x: x + 10)(1))

# 람다에는 변수를 새로 정의해서 사용할 수 없다
# lambda x: y = 10 ; x + y  이렇게 y를 정의해서 사용 할 수 없다
y = 10
print((lambda x: x + y)(1))


# map
# map(함수, x자리에 들어갈 자료형)
def plus_six(x):
    return x + 6

print(list(map(plus_six, [1,2,3])))

# 람다 표현식으로 바꿔보자

print(list(map(lambda x: x + 6, [1, 2, 3])))


# 람다 표현식과 map, filter, reduce 활용하기
# lambda 매개변수들: 식1 if 조건식 else 식2
# map은 리스트의 요소를 각각 처리하므로 lambda의 반환값도 요소야함

# 3의 배수만 string으로 변환하기
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: str(x) if x % 3 == 0 else x, a)))

# 람다 표현식에 조건부 표현식 사용하기
'''
- 람다 표현식 안에서 조건부 표현식 if,else를 사용할때 :(콜론)을 붙이지않음
- if, else 문법이 다르므로 주의해야한다
- 조건부 표현식은 식1 if 조건식 else 식2 형식으로 사용하며 식1은 조건식이 참일 때, 식2는 조건식이 거짓일 때 사용할 식
- 람다 표현식에서 if를 사용하면 else를 반드시 사용해야한다
- elif를 사용할 수 없다 그냥 if else if else로 이어가야한다
- 식1 if 조건식1 else 식2 if 조건식2 else 식3 
- 복잡하다면 그냥 함수를 만들어서 if, elif, else를 사용하는걸 권장
'''

# map에 객체를 여러 개 넣기
# - 두 리스트의 요소를 곱해서 새 리스트 만들기. 매개변수 갯수에 맞게 반복 가능한 객체도 콤바로 구분해서 넣으면 된다
c = [1, 2, 3, 4, 5]
d = [2, 4, 6, 8, 10]

print(list(map(lambda x,y: x * y, c, d)))


# filter
# 필터는 반복 가능한 객체에서 특정 조건에 맞는 요소만 가져오는데, filter에 지정한 함수의 반환값이 True일때만 해당 요소를 가져온다
def f(x):
    return x > 5 and x < 10

a = [8, 1, 24, 3, 7, 6]
print(list(filter(f, a)))

# lambda 표현식으로 만들어보자
print(list(filter(lambda x: x > 5 and x < 10, a)))


# reduce
# 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤 이전 결과와 누적해서 반환하는 함수. python3부터 내장함수가 아니라 functools 모듈에서 함수를 가져와야한다

def f(x, y):
    return x + y

a = [1, 2, 3, 4, 5]Three dimensional
언급하다
from functools import reduce

print(reduce(f, a))
'''
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
10 + 5 = 15

15를 반환
'''

# lambda 표현식으로 해보자
print(reduce(lambda x, y: x + y, a))
