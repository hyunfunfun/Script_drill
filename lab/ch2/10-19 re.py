import random

NofBall=eval(input())
NofSloat=eval(input())

sloat=[0]*NofSloat

for _ in range(NofBall):
    NofR=0
    for _ in range(NofSloat):
        if random.random()>0.5:
            print('R',end='')
            NofR+=1
        else:
            print('L',end='')
    sloat[NofR]+=1
    print()

Max=max(sloat)

for h in range(Max,0,-1):
    for n in range(NofSloat):
        if sloat[n] >= h:
            print('0',end='')
        else:
            print(' ',end='')
    print()