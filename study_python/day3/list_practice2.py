'''
화씨 온도(°F)를 섭씨 온도(°C)로 바꾸어주는 프로그램을 만들려고 합니다.

섭씨와 화씨의 관계식은 다음과 같습니다:

    섭씨 = (화씨 - 32) * 5 // 9


화씨 온도를 섭씨 온도로 변환해 주는 함수 fahrenheit_to_celsius를 써 보세요. 이 함수를 파라미터로 화씨 온도 fahrenheit를 받고, 변환된 섭씨 온도를 리턴합니다.

위 프로그램을 실행하면 아래처럼 출력되어야 합니다.
'''
# print(f"{c:.1f}")

# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(fahrenheit):
    # 코드를 입력하세요.
    c = (fahrenheit - 32) * 5 / 9
    return round(c, 1)


temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드를 입력하세요.
# temperature_list[0] = 44
i = 0
while i < len(temperature_list):
    temperature_list[i] = fahrenheit_to_celsius(temperature_list[i])
    # print(temperature_list[i])
    i += 1



print("섭씨 온도 리스트: " + str(temperature_list))  # 섭씨 온도 출력