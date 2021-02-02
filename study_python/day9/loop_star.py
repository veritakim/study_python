'''
계단식으로 별 출력하기

증첩 루프

for i in range(횟수)      # 바깥쪽 루프
    for j in range(횟수)  # 안쪽 루프
        가로 처리 코드
    세로 처리 코드
'''


for i in range(5):
    for j in range(5):
        print("*", end="")
    print()


for i in range(5):
    for j in range(5):
        print(f"j:{j}", end=" ")
    print(f"i:{i}\\n")



# 별 출력하기~
for i in range(5):
    for j in range(5):
        if j <= i:
            print("*", end="")
    print()


# 별 대각선으로 찍기
for i in range(5):
    for j in range(5):
        if i >= 1 and j < i:
            print(" ", end="")
        elif i == j:
            print("*", end="")
    print()


# 역 삼각형으로 별 출력
for i in range(5):
    for j in range(5):
        if i>0 and i > j :
            print(" ", end="")
        else:
            print("*", end="")
    print()

