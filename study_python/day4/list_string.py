# 문자열과 리스트
# 문자열 : 문자들의 나열, 리스트 : 자료형들의 나열
# 공통점이 있다

# 인덱싱이 가능하다
# 알파벳 리스트의 인덱싱
alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabets_list[0])
print(alphabets_list[1])


# 알파벳 문자열의 인덱싱
alphabets_string = 'ABCDEFGHIJ'
print(alphabets_string[0])
print(alphabets_string[1])
# for 반복문으로도 가능
for apb in alphabets_list:
    print(apb)

for apb_str in alphabets_string:
    print(apb_str)


# 슬라이싱이 가능하다
# 알파벳 리스트의 슬라이싱
alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabets_list[0:5])
print(alphabets_list[4:])
print(alphabets_list[:4])

# 알파벳 문자열의 슬라이싱
alphabets_string = 'ABCDEFGHIJ'
print(alphabets_string[0:5])
print(alphabets_string[4:])
print(alphabets_string[:4])



# 덧셈 연산이 가능하다
# 리스트의 덧셈 연산
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = list1 + list2
print(list3)

# 문자열의 덧셈 연산
string1 = '1234'
string2 = '5678'
string3 = string1 + string2
print(string3)



#len 함수 사용이 가능하다
# 리스트의 길이 재기
print(len(['H', 'E', 'L', 'L', 'O']))

# 문자열의 길이 재기
print(len("Hello, world!"))



'''
 차이점
'''
# 리스트는 수정이 가능하고 문자열은 수정을 할 수 없다
# 문자열 데이터 바꾸기
name = "codeit"
name[0] = "C"
print(name) # Error가 난다. 문자열은 바꿀 수 없다.

