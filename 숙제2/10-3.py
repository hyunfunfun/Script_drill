s = input('1과 100 사이의 정수 입력')

sList = s.split()

iList = [eval(i) for i in sList]

histogram = [0]*100
for i in iList:
    histogram[i-1] += 1

for i in range(100):
    if histogram[i]:
        print(i+1,'-',histogram[i],'번 나타납니다.')