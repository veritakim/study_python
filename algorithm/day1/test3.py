'''
 리그 경기횟수 맞추기
 참가할 총 팀 갯수를 입력해서 리그전이 몇 번 치뤄져야하는지 출력하라
'''

team = int(input())
num = 0
for i in range(1, team):
    num += i

print(num)
