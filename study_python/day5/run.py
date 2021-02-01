import calculator as cal  # 모듈 불러오기. 같은 폴더에 있는 파일을 불러올 수 있다
# from calculator import add, multiply  # 하나씩 불러오기
# from calculator import * # 전부 부르기 그렇지만 출처가 분명하지 않기 때문에 추천하지 않는다

'''
 불러오는 모듈의 이름이 너무 길다 
 알리아스를 줘서 바꿔 보자
'''
'''
print(calculator.add(3, 5))
print(calculator.substract(10, 5))
print(calculator.multiply(10, 5))
print(calculator.devide(10, 5)) 
'''

# 알리아스로 모듈 부르기

print(cal.add(3, 5))
print(cal.substract(3, 5))
