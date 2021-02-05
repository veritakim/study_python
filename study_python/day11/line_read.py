
# 리스트 형태로 가져오기
with open('hello.txt', 'r', encoding="UTF-8") as f:
    lines = f.readlines()
    print(lines)


# 파일의 내용을 한 줄씩 읽기
with open('hello.txt', 'r', encoding="UTF-8") as f:
  '''
   line = None
    while line != '':
        line = f.readline()
        print(line.strip('\n'))
  '''
  for l in f:
      print(l.strip('\n'))