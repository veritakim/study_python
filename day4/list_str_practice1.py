'''
함수 sum_digit은 파라미터로 정수형 num을 받고, num의 각 자릿수를 더한 값을 리턴합니다.

예를 들어서 12의 각 자릿수는 1, 2이니까 sum_digit(12)는 3(1 + 2)을 리턴합니다.

마찬가지로 486의 각 자릿수는 4, 8, 6이니까 sum_digit(486)은 18(4 + 8 + 6)을 리턴하는 거죠.

여러분이 해야 할 일은 두 가지입니다.

sum_digit 함수를 작성한다.
sum_digit(1)부터 sum_digit(1000)까지의 합을 구해서 출력한다.
'''


# 자리수 합 리턴
def sum_digit(num):
    sum = 0
    # 코드를 입력하세요.
    num1 = str(num)
    # return print(len(num1))

    if len(num1) == 1:
        sum = int(num1)
    else:
        for i in num1:
            sum = sum + int(i)
    return sum


# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
# 코드를 입력하세요.


list = []
sum2 = 0
for j in range(1, 1001):
    list.append(sum_digit(j))
for k in list:
    sum2 += k

print(sum2)
