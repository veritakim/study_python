# scope
'''
 scope : 변수가 사용 가능한 범위.
 - 로컬 변수 : 변수를 정의한 함수 내에서만 사용 가능
 - 글로벌 변수 : 모든 곳에서 사용 가능
 - 함수에서 변수를 사용하면, 로컬 변수를 먼저 찾고 나서 글로벌 변수를 찾음

'''
def my_function():
    x = 3
    print(x)

my_function()
# print(x)
# => error x는 정의된 적 없다고 뜬다 x는 함수안에서만 정의됐다. 로컬변수 함수 내에서만 사용 가능하다

x1 = 2
def my_function2():
    print(x1)

my_function2()
print(x1)

# x1는 글로벌 변수수

