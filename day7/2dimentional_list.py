'''
2차원 리스트 사용하기
   열   열   열   열
행
행
행
행

a = [[10, 20], [30, 40], [50, 60]]

    10 20
    30 40
    50 60
'''

a = [[10, 20], [30, 40], [50, 60]]

print(a[0][1]) # 20
print(a[2][0])

for x, y in a:
    print(x, y)

# for문 두 번 사용하기
for i in a:
    for j in i:
        print(j, end=" ")

    print()
print()


# for와 range 사용하기
for i in range(len(a)):   # 세로 크기
    for j in range(len(a[i])): # 가로 크기
        print(a[i][j], end=' ')
    print()

print()


# while 반복문을 사용해서
i = 0
while i < len(a):  # 반복할 때 리스트의 크기 활용
    x, y = a[i]     # 요소 두 개를 한꺼번에 가져오기
    print(x, y)
    i += 1



