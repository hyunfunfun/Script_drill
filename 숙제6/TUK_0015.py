def BtoDec(L,b):
    result=0 #L=[3,3,1,2], b=4, result=(((0x4+3)x4+3)x4+1)x4+2
    for i in L:
        result = result*b+i
        # print(result)
    return result

[b,N,M] = [eval(s) for s in input().split()]
Nlist = [eval(s) for s in input().split()]
Mlist = [eval(s) for s in input().split()]

N10=BtoDec(Nlist,b)
M10=BtoDec(Mlist,b)

P=N10*M10
Plist=[]
while P:
    Plist.insert(0, P%b)
    P //=b

print(len(Plist))
for i in Plist:
    print(i, end=' ')