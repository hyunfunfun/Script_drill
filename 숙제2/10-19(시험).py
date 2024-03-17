import random
nOfBalls = eval(input('콩의 개수:'))
nOfSlots = eval(input('슬롯의 개수:'))

slots = [0]*nOfSlots #슬롯의 개수 만큼 0으로 초기화

for i in range(nOfBalls):
    nOfR=0
    for j in range(nOfSlots-1):
        if random.random()>0.5:
            print('R',end='')
            nOfR +=1
        else:
            print('L',end='')
    print()
    slots[nOfR] += 1 # 해당 슬롯 빈도수 1증가

Max = max(slots) #최빈도수를 구한다
for h in range(Max,0,-1): #Max, Max-1 ... 1
    for i in range(nOfSlots): #슬롯의 개수만큼 반복
        if slots[i] >= h:
            print('0',end='')
        else:
            print(' ', end='')
    print()
