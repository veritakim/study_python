'''
 스탠다드 라이브러리
 int, flot, string 같은 자료형
 print, dir 같은 내장 함수
 유용한 기능을 제공하는 모듈들 (스탠다드 모듈)

 https://docs.python.org/ko/3/library/
'''

# math 모듈 수학관련 함수
import math

# math 함수 사용해보기
# math.log10()
# math.cos()

# random 함수
import random

random.randint(1, 20) # 1 부터 20까지 랜덤한 정수
random.uniform(1, 20) # 1 부터 20까지 랜덤한 소수


# datetime 날짜와 시간의 클래스
import datetime
today = datetime.datetime.today()
print(today.strftime("%A, %B, %dth %Y"))


# os Operating System 운영체제

# re 프로그래밍에서 Regular Expression(정규 표현식)은 특정한 규칙/패턴을 가진 문자열을 표현하는데 사용

import re
# 알파벳으로 구성된 단어들의 매칭
pattern = re.compile('^[A-Za-z]+$')
print(pattern.match('I'))
print(pattern.match('love'))
print(pattern.match('python3'))

print()

# 숫자가 포함된 단어들만 매칭
pattern = re.compile('.*\d+')
print(pattern.match('I'))
print(pattern.match('love'))
print(pattern.match('python3'))


# pickle 파이썬 오브젝트(객체)를 바이트 형식으로 바꿔서 파일에 저장할 수 있고, 저장된 오브젝트를 읽어올 수 있다
'''
 텍스트가 아닌 형식의 객체 파일을 저장하고 읽을 때 사용
'''
import pickle

# 딕셔너리 오브젝트
obj = {'my': 'dictionary'}

# obj를 filename.pickle 파일에 저장
# pickle.dump(data, file)
with open('filename.pickle', 'wb') as f:
    pickle.dump(obj, f)


# filename.pickle에 있는 오브젝트를 읽어옴
with open('filename.pickle', 'rb') as f:
    obj = pickle.load(f)

print(obj)


# json
# 오브젝트(객체)를 json 형식으로 바꿔준다. JSON 형식에 맞는 데이터(기본 데이터 타입들, 리스트, 딕셔너리)만 바꿀 수 있다
import json

# 딕셔너리 오브젝트
obj2 = {'my': 'dictionary'}

# obj2를 json 파일에 저장
with open('filename.json', 'w') as f:
    json.dump(obj2, f)

#filename.json 읽어오기
with open('filename.json', 'r') as f:
    obj2 = json.load(f)

print(obj2)


# copy, sqlite3