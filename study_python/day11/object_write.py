'''
파이썬 객체를 파일에 저장하기 , 가져오기

객체를 파일에 저장하는 pickle 모듈을 제공함

저장하는 과정을 피클링, 읽어오는 과정을 언피클링이라고 한다
'''

import pickle


name = 'mark'
age = 24
address = 'seoul seocho-gu banpo-dong'
score = {'korea': 90, 'english' : 100, 'math' : 85, 'science' : 98}

with open('mark.p', 'wb') as f:
    pickle.dump(name, f)
    pickle.dump(age, f)
    pickle.dump(address, f)
    pickle.dump(score, f)