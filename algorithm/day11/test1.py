'''
 최대값 최소값 구하기.
첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.
첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.
'''

count = int(input())
num = []
min = 0
max = 0
for i in range(count):
    num.append(int(input()))

min = num[0]
max = num[0]

for j in num:
    if min > j:
        min = j
    else:
        min = min
    if max < j:
        max = j
    else:
        max = max
print(min, max)



