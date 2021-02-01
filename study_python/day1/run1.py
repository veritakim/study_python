# area 모듈에서 함수만 불러오기
# from area import circle, square


# print(circle(2))



# 모듈 이름 바꿔주기
# import area as ar
#
# print(ar.square(2))

# 모듈에서 함수 이름을 바꿔서 호출하기
# from area import square as sq, circle as ci
# print(sq(2))
# print(ci(2))

# 모듈에서 모든 함수 데려오기 권장하지 않는다
from area import *
print(square(2))
print(circle(2))