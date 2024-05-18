N = eval(input())


M = []

for i in range(1,N+1):
    row=[]
    n = i
    for j in range(N*2-1):
        if j==N-i:
            for _ in range(i):
                row.append(n)
                n-=1
            n+=1
            for _ in range(i-1):
                n += 1
                row.append(n)
        else:
            row.append('.')
    M.append(row)


for i in range(len(M)):
    for j in range(len(M[0])):
        if j==len(M[0])-1:
            print(M[i][j],end='')
        else:
            print(M[i][j],end=' ')
    print()