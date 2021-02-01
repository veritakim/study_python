num1 = int(input())
for i in range(1, num1+1):
    for j in range(num1 - i):
        print(" ", end="")
    for k in range(0, i):
        print("*", end="")
    print()


