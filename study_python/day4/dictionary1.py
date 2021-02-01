# 사전
# key : value 하나의 쌍을 이룬다
my_dictionary = {
    5: 25,
    2: 4,
    3: 9
}
print(type(my_dictionary)) # class dict

# 사전의 값을 받아오기 key 값을 넣어준다
print(my_dictionary[3])

# 사전에 값 넣어주기
my_dictionary[9] = 12
print(my_dictionary)


'''
 리스트와 사전의 차이
  리스트 : 인덱스의 순서대로. 인덱스는 정수
  사전 : 그냥 키와 밸류 쌍으로, 인덱스가 정수일 필요없다
'''
