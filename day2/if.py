tem = 16
if tem <= 10:
    print("자켓을 입는다.")
else:
    print("자켓을 입지 않는다.")


# elif문 else + if java의 else if 와 같다

'''
학생들에게 최종 성적을 알려 주는 '학점 계산기'를 만들려고 합니다.

이 수업에는 50점 만점의 중간고사와 50점 만점의 기말고사가 있는데요. 두 시험의 점수를 합해서 최종 성적을 내는 방식입니다. 규칙은 다음과 같습니다.

A: 90점 이상
B: 80점 이상 90점 미만
C: 70점 이상 80점 미만
D: 60점 이상 70점 미만
F: 60점 미만
'''
def print_grade(midterm_score, final_score):
    total = midterm_score + final_score
    # 코드를 쓰세요.
    if total >= 90:
        print("A")
    elif total < 90 and total >= 80:
        print("B")
    elif total < 80 and total >= 70:
        print("C")
    elif total < 70 and total >= 60:
        print("D")
    else:
        print("F")


# 테스트
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)


'''
while문과 if문을 활용하여, 100 이하의 자연수 중 8의 배수이지만 12의 배수는 아닌 것을 모두 출력하세요.

예를 들어서 16은 8의 배수이지만 12의 배수가 아니니까 조건에 부합합니다. 하지만 48은 8의 배수이면서 12의 배수이기도 해서 조건에 부합하지 않습니다.
'''
i1 = 1
while i1 <= 100:
    if i1 % 8 == 0 and i1 % 12 != 0:
        print(i1)
    i1 += 1


'''
10보다 작은 2 또는 3의 배수는 2, 3, 4, 6, 8, 9이며, 이들의 합은 32입니다.

while문과 if문을 활용하여, 1,000보다 작은 자연수 중 2 또는 3의 배수의 합을 출력하는 프로그램을 써 보세요.
'''
sum = 0
i = 1
while i < 1000:
    if i % 2 == 0 or i % 3 == 0:
        sum += i
    i += 1

print(sum)


'''
정수 n의 약수는 n을 나누었을 때 나누어 떨어지는 수입니다. 만약 정수 i가 정수 n의 약수라면, n을 i로 나누었을 때 나머지가 0이 나와야 하는 거죠.

정수 120의 약수를 모두 출력하고, 총 몇개의 약수가 있는지 출력하는 프로그램을 써 보세요
'''


a = 1
total = 0
while a <= 120:
    if 120 % a == 0:
        print(a)
        total += 1
    a += 1
print(f"120약수의 총 갯수는 {total}개 입니다.")



'''
1988년 쌍문동에 사는 택이는 바둑 대회 우승 상금으로 5,000만원을 받았습니다. 하지만 바둑 외에는 아는 게 없으니, 이웃 어른들에게 이 돈으로 무엇을 해야 할지 물어보기로 하였습니다.

은행에서 근무하는 동일 아저씨는 은행에 돈을 맡겨서 매년 이자로 12%씩 받는 것을 추천하셨습니다. 1년 후인 1989년에는 5,000만원의 12% 이자인 600만원이 더해져 5,600만원이 된다고 하면서요.

이 이야기를 들은 미란 아주머니는 고작 12% 때문에 생돈을 은행에 넣느냐며, 얼마 전 지어진 은마아파트를 사라고 추천하셨습니다. 당시 은마아파트의 매매가는 5,000만원이었죠.

2016년 기준 은마아파트의 매매가는 11억원인데요. 1988년 은행에 5,000만원을 넣었을 경우 2016년에는 얼마가 있을지 계산하여, 동일 아저씨와 미란 아주머니 중 누구의 말을 듣는 것이 좋았을지 판단해 보세요. 2016년 은행에 얼마가 있을지는 꼭 while문을 사용해서 계산해 주세요!

2016년에 은행에 저축해 둔 금액이 더 크면, *원 차이로 동일 아저씨 말씀이 맞습니다.가 출력되도록 하세요. 반대로 은마아파트의 가격이 더 크면, *원 차이로 미란 아주머니 말씀이 맞습니다.가 출력되도록 하세요. 여기서는 꼭 if문을 사용해 주세요!
'''

bank = 50000000
year = 1988
apt = 1100000000


while year < 2016:
    bank += bank * 0.12
    year += 1


bank = int(bank)


if bank - apt > 0:
    tt = bank - apt
    print(f"{tt}원 차이로 동일 아저씨 말씀이 맞습니다.")
else:
    tt = apt - bank
    print(f"{tt}원 차이로 미란 아주머니 말씀이 맞습니다.")

'''
if bank - apt > 0:
    price = bank - apt
    print(f"{price}원 차이로 동일 아저씨 말씀이 맞습니다.")
else:
    price = apt - bank
    print(f"{price}원 차이로 미란 아줌마 말씀이 맞습니다.")

'''
