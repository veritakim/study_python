'''
 조건문
 if xxx :    xxx자리에는 boolean 데이터 타입이 와야하 한다
     yyy
 else:
     zzzz   아니라면 zzz를 실행하라
'''

# input() Java에서 Scanner와 같은 역할
user_id = input('id?')
user_pwd = input('password?')
if user_id == 'egoing':
    if user_pwd == '111111':
        print('Hello master')
    else:
        print('who R U?')
else:
    print('Access denied')
