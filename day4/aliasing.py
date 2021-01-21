x = [2, 3, 5, 7, 11]
y = x
y[2] = 4
print(x)
print(y)

# print(x) = [2, 3, 5, 7, 11]
# print(y) = [2, 3, 4, 7, 11] 가 나올것 같지만 print(x) print(y) 둘 다 [2, 3, 4, 7, 11]가 나온다

# x의 값을 유지하며 y의 값을 변환시키는 방법은 없을까 ?
x = [2, 3, 5, 7, 11]
y = list(x) # 새로운 리스트로 복사
y[2] = 4
print(x)
print(y)
