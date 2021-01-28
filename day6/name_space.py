# 네임 스페이스 : 파일에서 정의된 모든 이름
from area import circle, square as sq

# print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'circle', 'square'] 현재 이 파일에 정의된 네임 스페이스들

# 만약 이 파일에서 square 함수를 재정의 한다면 어떻게될까?
def square(len):
    return 4 * len

print(square(3)) # 이름이 중복된다면 나중에 정의된 함수를 사용한다.

# 중복되지 않게 가져오는 방법?
'''
1. area의 square 함수를 다른 이름으로 가져온다. 알리아스를 준다.
square as sq
'''
print(dir()) # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'circle', 'sq', 'square']
print(sq(3))