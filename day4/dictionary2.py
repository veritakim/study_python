# 사전 활용하기
my_family = {
    '아빠': '이민형',
    '엄마': '김마베',
    '아들': '이박지성',
    '딸': '이나은'
}

# .values() : 밸류값이 뭐가 있는지 알고싶을 때
print(my_family.values()) # dict_values(['이민형', '김마베', '이박지성', '이나은'])
# 값 in : 값이 있는지 알고 싶을 때
print('이민형' in my_family.values()) # 값이 있으면 True, 없다면 False를 반환해준다
print('서영호' in my_family.values()) # False

# for문을 이용해 값을 하나씩 출력해보자
for value in my_family.values():
    print(value)

# key값을 알고싶다면
print(my_family.keys())

# key값을 전체 출력해보자
for key in my_family.keys():
    print(key)

# .items() : key와 value 한번에 받아오기
for key, value in my_family.items():
    print(key, value)