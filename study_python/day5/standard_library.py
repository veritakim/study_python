# standard library(표준 라이브러리)
'''
 math , random, os ...
'''
import random
import os
import datetime


# random : 랜덤한 숫자를 생성하기 위한 다양한 함수 제공
# - randint(a, b) a, b두 수 사이에 만족하는 어떠한 랜덤한 정수 N을 리턴 ex) randint(1, 20) 이면 1이상 20이하의 정수 사이의 값을 준다
print(random.randint(1, 20))

# uniform(a, b) 두 수 사이의 랜덤한 소수를 리턴한다.
print(random.uniform(1, 20))


# datetime 날짜와 시간을 다루기 위한 datetime(year, month, day, hour, minute, second)
# 값 생성해보기
pi_day = datetime.datetime(2020, 3, 14)
print(pi_day) # 2020-03-14 00:00:00
print(type(pi_day)) # <class 'datetime.datetime'>

# 시간 설정하기
fi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(fi_day) # 2020-03-14 13:06:15

# 오늘 날짜
to_day = datetime.datetime.now()
print(to_day)

# timedelta  두 datetime 값 사이의 기간을 알고 싶으면, 마치 숫자 뺄셈하듯 사용하면 된다
print(to_day - fi_day) # 317 days, 4:27:08.168655
print(type(to_day - fi_day)) # <class 'datetime.timedelta'>

# 반대로 timedelta를 생성해서 datetime값에 더할 수 있다
my_timedelta = datetime.timedelta(days=5, hours=3, minutes=10, seconds=30)
print(to_day) # 2021-01-25 17:35:50.453016
print(to_day + my_timedelta) # 2021-01-30 20:45:57.551194

# 해부하기
print(to_day)
print(to_day.year) # 연도
print(to_day.month) # 월
print(to_day.day) # 일

# datetime 포매팅
# datetime값을 출력하면 보기에 어렵다. 보기 쉽게 하기위해 strtime을 사용한다
print(to_day.strftime("%A, %B %dth %Y")) # Monday, January 25th 2021

'''
포맷 코드 (대문자, 소문자는 소문자는 짧은 버전 mon, 대문자는 긴 버전 Monday)
%a %A : 요일 
%w : 요일 숫자버전( 0 ~ 6, 0은 일요일)

%d : 일

%b %B : 월
%m : 월 숫자버전 ( 1 ~ 12 )

%y %Y : 연도

%H : 시간 풀버전 00 ~ 23
%ㅣ : 시간 00 ~ 12

%p : am/pm

%M : 분(00 ~ 59)

%S : 초(00 ~ 59)

%f : 마이크로초

%Z : 표준시간대 PST

%j : 1년중 며칠째인지(001 ~ 366)

%U	: 1년 중 몇 주째인지 (00~53, 일요일이 한 주의 시작이라고 가정)

%W	1년 중 몇 주째인지 (00~53, 월요일이 한 주의 시작이라고 가정)	35
'''



print(os.getlogin()) # 현재 로그인 된 계정
print(os.getcwd()) # 현재 파이썬의 저장된 경로


