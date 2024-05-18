NofBall = eval(input())
NofSloat = eval(input())

sloat = [0]*NofSloat

for _ in range(NofBall):
    NofR=0
    RL = input()
    for i in RL:
        if i=='R':
            NofR+=1
    sloat[NofR]+=1

Max=max(sloat)

for h in range(Max,0,-1):
    for n in range(NofSloat):
        if h<=sloat[n]:
            print('*',end='')
        else:
            print('.',end='')
    print()
