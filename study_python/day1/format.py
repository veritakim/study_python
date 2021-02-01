# 오늘은 2021년 1월 18일 입니다
year = 2021
month = 1
day = 18

print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "일 입니다.")
print("오늘은 {}년 {}월 {}일 입니다.".format(year, month, day))

date_string = "오늘은 {}년 {}월 {}일 입니다."
print(date_string.format(year, month, day))

# format 파라미터 순서 바꾸기
print("저는 {1}, {0}, {2}를 좋아합니다".format("유재석", "김종국", "하하"))

# 파라미터의 소수점 가공하기 ex) 소수점 둘째자리까지만  :.자릿수f   정수로 표현하고 싶다면 :.0f
num1 = 1
num2 = 2
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num1, num2, num1 / num2))

# 새로운 방식 f-string
name = "유재석"
age = 32

print(f"제 이름은 {name}이고 {age}살입니다.")