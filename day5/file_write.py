'''
with open('new_file.txt', 'w') as f:
    f.write("Hello world\n")
    f.write("I'm hero") # 마지막 실행을 덮어 쓴 다.
'''

with open('new_file.txt', 'a') as f:  # w자리를 a로 변경했다. append 기존의 내용도 남아있고 그 뒤에 글을 추가함
    f.write("Hello world\n")
    f.write("I'm hero\n") # 마지막 실행을 덮어 쓴 다.
