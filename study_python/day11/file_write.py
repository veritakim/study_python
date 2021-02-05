'''
 파일 문자열 쓰기

 파일객체 = open(파일이름, 파일모드)
 파일객체.write('문자열')
 파일객체.close()

'''

with open('hello.txt','w') as f:
    f.write('Hello, World!')


