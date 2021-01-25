# file_read 에서 sell.txt를 프린트 했을 때
'''
1일 : 얼마

2일: 얼마

중간에 엔터가 하나 더 쳐진다. 왜냐하면 print 자체가 엔터의 기능이 있는데 텍스트에도 엔터가 들어가서 두 번의 엔터 기능이 됐다

\n
'''

# .strip() : 화이트 스페이스. 글자들 사이 이외의 빈 공백들을 처리
with open('data/sell.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        print(line.strip())
