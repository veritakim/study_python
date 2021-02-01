'''
 모듈
 게임 프로그램을 만든다고 가정한다면, 만약 한 파일에 코드를 다 집어넣는다면 어느 부분이 어떤 기능을 하는지 어렵고 찾기도 힘들다.
 이러한 단점을 보완하고자 파일을 같은 기능대로 분류하여 사용하는 것을 모듈이라고 한다.
 모듈은 코드를 재사용 할 수 있다는 장점이 있다

 모듈을 사용하는 방법
  import 파일이름

 모듈에서 특정한 함수만 사용하고 싶다면. 콤마를 사용해 여러 개가 나열 가능하다
 from 파일이름 import 함수이름

 알리아스 주기 : 모듈의 이름이 너무 긴 경우 as를 사용해 알리아스를 줄 수 있다
 import area as ar
 ar로 함수를 불러올 수 있다
'''


'''
dir(모듈이름) 모듈에서 정의한 클래스와 함수를 알려준다

__ 가 붙은 것은 특수변수 던더(더블 언더 스코어) 라고 읽는다
파이썬이 내부적으로 관리한다  
'''
# import cil
# print(dir()) 아무것도 넣지 않는다면 현재 지금 module.py의 정의된 이름들이 확인된
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'cil']

from cil import invert, display
# import cil의 함수들을 직접 호출했을 때
print(dir()) # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'display', 'invert']






