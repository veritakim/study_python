'''
 문자열 조작하기

 replace는 조작만 해주지 결과값을 바꾸지 않는다
'''
# ex)
s = 'Hello, world!'
print(s.replace('world', 'Python')) # 보여주기 용. s값이 바뀐게 아니다
print(s)

# s의 값을 바꾸고 싶다면
s = s.replace('world', 'Python')
print(s)

# 문자 바꾸기
'''
translate는 문자열 안의 문자를 다른 문자로 바꿈
str.maketrans('바꿀문자', '새문자')로 변환 테이블을 만듬
'''
table = str.maketrans('aeiou', '12345') # aeiou 를 각각 12345 a는1 e는2 i는3 o는4로 바꾸라는 말
'apple'.translate(table) # apple를 table에 있는 문자들로 바꾸라는 말. aeiou를 12345로
# 그래서 apple에는 table에 ae가 있으니까 그 자리를 1ppl2 로 대체한다는 말
print('apple'.translate(table))


'''
문자열과 문자열 리스트 연결하기
'구분자(공백허용)'join[,,, 연결할 문자열들 ,로 구분]
'''
st = ' '.join(['apple', 'banana', 'orange', 'grape'])
print(st)


# 대문자 소문자 바꾸기. 바꾸고 싶은 문자열.upper() : 다 대문자로, 문자열.lower() : 다 소문자로


# 문자열 공백 삭제하기
'''
lstrip() : 왼쪽 공백 삭제
rstrip() : 오른쪽 공백 삭제
strip()  : 양쪽 공백 삭제

특정 문자도 삭제할 수 있다
(',.')안에 넣으면  콤마와 쩜을 삭제하라는 의미
'''
t = '   Python      '.rstrip()
print(t)


# 정렬하기
'''
'문자열'.ljust(문자수) : 문자수만큼 길이가 되는데 왼쪽부터 정렬하라
'문자열'.rjust(문자수) : 오른쪽부터 정렬하라
'문자열'.center(문자수) : 가운데 정렬. 공백이 홀수가 된다면 왼쪽에 공백이 한 칸 더 들어감
'''

print('Apple'.ljust(10)) # Apple     /
print('Apple'.rjust(10)) #      Apple/
print('Apple'.center(10)) #   Apple   /


# 메서드 체이닝. 문자열 조작은 줄줄이 메서드를 사용해줄 수 있다.
'strawberry'.upper().rjust(10) # 스트로베리를 대문자로 바꾸고 10자리수의 문자열에 오른쪽 정렬을 하라는 뜻.

# 문자열 왼쪽에 0채우기
# 문자열.zfill(문자열수)
'hello'.zfill(10) # 10칸 중 오른쪽에 hello를 채우면 왼쪽에 공백 5자리에 0으로 채워라




# 문자열 위치 찾기
'''
문자열.find(찾을 문자열) 인덱스의 위치를 반환. 없다면 -1을 반환한다
.rfind 오른쪽에서 부터 인덱스를 반환. 인덱스 위치는 바뀌지 않는다.
.index 왼쪽부터 인덱스를 반환. 없으면 오류. 가장 먼저 찾는 인덱스를 반환시킨다
.rindex
'''

# 문자열 개수 세기 count()
print('apple'.count('p')) # 2