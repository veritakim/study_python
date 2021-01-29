# for문으로 1차원 리스트 만들기
a = [] # 빈 리스트 새성

for i in range(10):
    a.append(i)

print(a)


# 2차원 리스트 만들기
b = []
for i in range(3):
    line = []           # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(2):
        line.append(0)  # 안쪽 리스트에 0추가
    b.append(line)      # 전체 리스트에 안쪽 리스트를 추가

print(b)

# 리스트 표현식으로 2차원 리스트 만들기
c = [[0 for j in range(2)] for i in range(3)]
print(c)
# [[0] * 2 for i in range(3)] 으로 표현할 수 있음



# 톱니형 리스크 만들기
e = [3, 1, 3, 2, 5]
f = []

for i in e:  #e는 안쪽의 for문이 다 돌고 i는 3,1,3,2,5차례대로 돈다. range가 아니라 in이다
    line = []
    for j in range(i):
        line.append(0) # [] 먼저 저장
    f.append(line)   # [[]] 저장

print(f)