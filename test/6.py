N=eval(input())
M=[]
for _ in range(N):
    row=[input().split()]
    M.append(row)

A,B,C,D = map(eval,input().split())

for i in range(len(M)):
    sum=0
    for j in range(len(M[i])):
        sum+=M[i][0]
    if A>sum:
