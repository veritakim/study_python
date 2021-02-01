'''
별찍기
입려된 수만큼 별이 증가하는 출력상태를 만들어라
'''

num1 = int(input())


for i in range(1, num1+1):
    for j in range(0, i):
        print("*", end="")
    print()
