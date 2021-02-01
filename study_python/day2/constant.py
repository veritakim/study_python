# 상수 (constant)
# 바뀌지 않는 수. 모든 문자를 대문자로 써줘야한다.(숫자)

PI = 3.14 # 원주율 파이

# 반지름을 받아서 원의 넓이 계산
def cal(r):
    return PI * r * r

radius = 4
print(f"반지름이 {radius}면, 넓이는 {cal(radius)} 이다.")

radius = 6
print(f"반지름이 {radius}면, 넓이는 {cal(radius)} 이다.")

radius = 7
print(f"반지름이 {radius}면, 넓이는 {cal(radius)} 이다.")