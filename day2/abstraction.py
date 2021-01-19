# 변수
# 함수 실행순서

'''


def hello():
    print("Hello")
    print("to the world")

print("함수호출 전")
hello()
print("함수호출 후")
'''

# return문 제대로 이해하기
'''
 return문의 역할
  - 값 돌려주기
  - 함수 즉시 종료
'''
# example
def square(x):
    print('함수시작')
    return x * x
    print('함수끝') #Dead code 위에 return이 함수를 종료하기 때문에 출력되지 않는다

print(square(3))
print('Hello~')


# return과 print의 차이
'''
 return은 값을 돌려 주지만 출력해주지는 않는다
'''


#옵셔널 파라미터
'''
파라미터에게 '기본값(default value)'을 설정할 수 있다
기본값을 설정해 두면, 함수를 호출할 때 꼭 파라미터에 값을 안 넘겨 줘도 된다. 이런 파라미터를 '옵셔널 파라미터(optional parameter)'라고 한다. 
필수로 넘겨 줄 필요가 없으니까 '옵셔널'이라고 한다.
참고로 옵셔널 파라미터는 모두 마지막에 있어야 한다.
'''
def myself(name, age, nationality="한국"):
    print(f"내 이름은 {name}")
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))


myself("코드잇", 1, "미국")  # 옵셔널 파라미터를 제공하는 경우
print()
myself("코드잇", 1)  # 옵셔널 파라미터를 제공하지 않는 경우

# 'syntactic sugar'
'''
# 다음 두 줄은 같습니다
x = x + 1
x += 1

# 다음 두 줄은 같습니다
x = x + 2
x += 2

# 다음 두 줄은 같습니다
x = x * 2
x *= 2

# 다음 두 줄은 같습니다
x = x - 3
x -= 3

# 다음 두 줄은 같습니다
x = x / 2
x /= 2

# 다음 두 줄은 같습니다
x = x % 7
x %= 7
'''