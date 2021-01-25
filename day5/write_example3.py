'''
고급단어장

지난 실습 과제에서 단어장 퀴즈 프로그램을 만들었는데요. 학생들이 문제의 순서가 매번 똑같아서 재미가 없다고 합니다.

이번에는 random 모듈과 사전(dictionary)을 이용해서 vocabulary.txt의 단어들을 랜덤한 순서로 내도록 프로그램을 바꿔 보세요.

같은 단어를 여러번 물어봐도 괜찮고, 프로그램은 사용자가 알파벳 q를 입력할 때까지 계속 실행됩니다.
'''
import random
dict = {}

with open("vocabulary.txt", "r", encoding="UTF=8") as f:
    for line in f:
        str = line.strip().split(": ")
        eng, kor = str[0], str[1]
        dict[eng] = kor


    while True:
        key = list(dict.keys())
        index = random.randint(0, len(key) - 1)
        eng_word = key[index]
        kor_word = dict[eng_word]

        riddle = input(f"{kor_word}: ")
        if riddle == eng_word:
            print("맞았습니다.")
        elif riddle == 'q':
            break
        elif riddle != eng_word:
            print(f"틀렸습니다. 정답은 {eng_word}입니다.")
