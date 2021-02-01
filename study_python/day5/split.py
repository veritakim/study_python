# split 자르기
my_string = "1. 2. 3. 4. 5"
# print(my_string.split(". "))

full_name = "Kim. Yuna"
# print(full_name.split(". "))
name_data = full_name.split(". ")
last_name = name_data[0]
first_name = name_data[1]
# print(f"당신의 이름은 {first_name} {last_name}입니다.")

# split() 공백을 주면 모든 공백을 제거해 준다
numbers = "   \n\n  2  \t  3  \n  5   7  11  \n\n".split()
print(numbers)
# 주의점. split을 했을 때 숫자들은 int가 아니라 string이다
print(numbers[0]+numbers[1]) # 23이 출력
# 정수를 사용하고 싶다면
print(int(numbers[0]) + int(numbers[1])) # 5 출력