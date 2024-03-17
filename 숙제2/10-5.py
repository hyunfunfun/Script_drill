s = input('10개 개수 정수 입력:')

items = s.split()
numbers = [eval(x) for x in items]
List = []
for number in numbers:
    if not number in List:
        List.append(number)
print('중복을 제거한 고유한 숫자:',List)