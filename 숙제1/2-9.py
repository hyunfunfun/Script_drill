f = eval(input("화씨 -58F 와 41F 사이 입력:"))
s = eval(input("풍속 mph로 입력:"))

windchill = 35.74 + 0.6215 * f - 35.75 * s ** 0.16 + 0.4275 * f * s ** 0.16
print("체감온도는 ",windchill)