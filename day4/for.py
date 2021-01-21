# for 반복문

# 1 - 10 까지 출력해보자
num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# i 는 num1의 len만큼 돌려준다
for i in num1:
    print(i)



# range 함수
# 1 - 100까지를 출력해야한다면, 리스트에 1부터 100 까지 넣어줘야 한다. num2 = [1, 2, 3, 4, ... , 99, 100] 다 입력해줄 수 없다
'''
 range(stop) : 0부터 stop-1 까지 범위
 range( start , stop ) : start 부터 stop-1 까지의 범위
 range(start, stop, step) : start부터 stop-1 까지 step만큼 간격
 
 장점 : 간편하고 깔끔, 메모리를 효율적으로 사용
'''

for j in range(3, 11):
    print(j) # 3,4,5,6,7,8,9,10

for j in range(1, 11, 2):
    print(j) # 1, 3, 5, 7, 9