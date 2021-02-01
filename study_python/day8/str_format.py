'''
 문자열 서식 지정자와 포매팅 사용하기
'''

# 서식 지정자 문자열 넣기
# %s %'문자열' s에 문자열이 들어감
print('I am %s' %'james') # I am james

# 서식 지정자 숫자 넣기
# %d %숫자
print('I am %d old.' %20) # I am 20 old.

# 서식 지정자 소수 넣기
# %f %숫자
print('%f' %2.3) # 2.300000
# 소숫점 자리수 지정 f앞에 .과 자릿수를 지정해주면 된다.
print('%.2f' %2.3) # 2.30
print('%.3f' %2.3) # 2.300

# 서식 지정자로 문자열 정렬하기
# %길이s %문자열 왼쪽부터 정렬
print('%10s' %'james') #       james
# 오른쪽 정렬하기
print('%-10s' %'james') # james

# 값을 여러 개 넣기
# %d %s %f %(문자, 숫자, 숫자)  괄호로 묶어주고 콤마로 구분한다
print('Today is %d %s' %(1, 'monday')) # Today is 1 monday


# format
# {index}.format(값). 여러 개 할때는 값의 넣을 순서만 주의해주면 된다. 인덱스를 생략하면 format()안에 있는 순서대로 넣어진다
print('Hello {0} {1} {2}'.format(21, 'welcome', 'Python')) # Hello 21 welcome Pyton
# 이름을 지정할 수 있다.
print('Hello {language} {ver}'.format(language='Python', ver=3.0))

# language = python ver= 3.0 f."{language} {ver}" 로 써줄 수도 있다


# format 메서드로 문자열 정렬하기
# '{인덱스:<길이}'.format(값)
print('{0:<10}'.format('python')) # python    / 왼쪽 정렬
print('{0:>10}'.format('python')) #     python/ 오른쪽 정렬


# 숫자 개수 맞추기
#  {}를 사용할 때는 인덱스나 이름 뒤에 :(콜론)을 붙이고  03d처럼 0과 숫자 개수를 지정하면 됨
print('%03d' %1) # 001
print('{0:03d}'.format(1)) # 001

# 소수점 이하 자릿수를 지정하고 싶을 때!
# %0총숫자수.소수점수 총수만큼
print('%04.2f' %3.2) # 3.20
print('{0:04.2f}'.format(3.2)) # 3.20

# {0:채울것>자릿수}
print('{0:1<10}'.format(12)) # 1211111111
print('{0:1>10}'.format(12)) # 1111111112

# 만약 채울것을 써주지 않는다면 공백이 들어간다.
print('{0: >10}'.format(40)) #         40/
