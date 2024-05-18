A,B = map(eval,input().split())

n=1
M=[]
for i in range(A):
    row=[]
    for j in range(B):
        row.append(n)
        n+=1
    M.append(row)
print('M')
for i in range(len(M)):
    for j in range(len(M[0])):
        if j==len(M[0])-1:
            print(M[i][j],end='')
        else:
            print(M[i][j],end=' ')
    print()

R=[[M[r][c] for r in range(A-1,-1,-1)]for c in range(B)]
print('R')
for i in range(len(R)):
    for j in range(len(R[0])):
        if j==len(R[0])-1:
            print(R[i][j],end='')
        else:
            print(R[i][j],end=' ')
    print()

L=[[M[r][c] for r in range(A)]for c in range(B-1,-1,-1)]
print('L')
for i in range(len(L)):
    for j in range(len(L[0])):
        if j==len(L[0])-1:
            print(L[i][j],end='')
        else:
            print(L[i][j],end=' ')
    print()

T=[[M[r][c] for r in range(A)]for c in range(B)]
print('T')
for i in range(len(T)):
    for j in range(len(T[0])):
        if j==len(T[0])-1:
            print(T[i][j],end='')
        else:
            print(T[i][j],end=' ')
    print()