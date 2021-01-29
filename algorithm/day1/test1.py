'''
약수 구하기
양의 정수를 입력받고 그 수의 약수를 출력하세요
'''

integer = input()
num = int(integer)
num2 = ""
for j in range(1,num+1):
    if num % j == 0:
       num2 += str(j) + " "
    else:
        continue

print(num2)