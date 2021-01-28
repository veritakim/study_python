'''
1. cil.py 파일에 있는 invert(img) 함수를 구현해 주세요.
2. main 파일이 잘 실행되도록 코드를 완성해 주세요.
'''
# cil 모듈을 임포트해 주세요
### 코드를 작성해 주세요 ##
import cil
# cil 모듈의 display 함수를 직접 임포트해 주세요
### 코드를 작성해 주세요 ###
from cil import display

img1 = cil.read_image('img1')
img2 = cil.read_image('img2')

inverted_img1 = cil.invert(img1)
inverted_img2 = cil.invert(img2)

print('원본 이미지')
print('\nimage1:')
display(img1)
print('\nimage2:')
display(img2)

print('\n색상 반전된 이미지')
print('\nimage1:')
display(inverted_img1)
print('\nimage2:')
display(inverted_img2)

# 채점 코드
print()
print('cil' in dir())
print('display' in dir())