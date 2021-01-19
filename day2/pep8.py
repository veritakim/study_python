# PEP8 style
'''
 파이썬에서 사용하는 코딩 스타일
'''


# 이름 규칙 :
# 무든 변수와 함수 이름은 소문자로, 단어가 이어질 경우 _ 로 나눠준다.
# 모든 상수 이름은 대문자로 표기한다


# bad
someVariableName = 1
SomeVariableName = 1

def someFunctionName():
    print("Hello")


# good
some_variable_name = 1

def some_function_name():
    print("Hello")


# 화이트 스페이스 들여쓰기는 무조건 스페이스 4번
# bad (스페이스 2개)
def do_something():
  print("Hello, world!")


# bad (스페이스 8개)
i = 0
while i < 10:
        print(i)


# good (스페이스 4개)
def say_hello():
    print("Hello, world!")


# 함수 정의
# 함수 정의 두 개 이상일 경우 함수들 사이에 빈 줄이 두 줄이 존재해야 한다
# bad
def a():
    print('a')
def b():
    print('b')

def c():
    print('c')



# good
def a():
    print('a')


def b():
    print('b')


def c():
    print('c')


# 괄호 안
# 괄호 안에는 띄어쓰기를 하지 말어라
# bad
spam( ham[ 1 ], { eggs: 2 } )


# good
spam(ham[1], {eggs: 2})


# 함수 괄호
# 함수를 정의하거나 호출할 때, 함수 이름과 괄호 사이에 띄어쓰기를 하지 마세요
# bad
def spam (x):
    print (x + 2)


spam (1)


# good
def spam(x):
    print(x + 2)


spam(1)