A,B = input().split()

M=[]
find=True
a,b=0,0
for i in range(len(B)):
    for j in range(len(A)):
        if B[i]==A[j]:
            a,b=j,i
            find=False
            break
    if find==False:
        break


for i in range(len(B)):
    for j in range(len(A)):
        if i==b:
            print(A[j],end='')
        elif j==a:
            print(B[i],end='')
        else:
            print('.',end='')
    print()