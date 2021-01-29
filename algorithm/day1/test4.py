'''
입력받은 횟수 만큼
두 수의 덧샘 하기
'''

num1 = int(input())
sum = []
amount = 0
for i in range(1, num1+1):
    a = input().split(" ")
    amount = int(a[0]) + int(a[1])
    sum.append(str(amount))

for j in sum:
    print(j)
