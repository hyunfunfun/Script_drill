s = input('정수 리스트 입력:')

s.split()

items = s.split()

numbers = [eval(x) for x in items]
numbers.reverse()

for x in numbers:
    print(x)