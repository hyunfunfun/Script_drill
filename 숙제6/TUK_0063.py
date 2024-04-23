def print2DList(M):
    for r in range(len(M)):
        for c in range(len(M[0])):
            if c == len(M[0])-1:
                print(M[r][c])
            else:
                print(M[r][c],end=' ')

A,B = map(eval, input().split())
M=[]
n=1
for r in range(A):
    row = []
    for c in range(B):
        row.append(n)
        n+=1
    M.append(row)

print('M')
print2DList(M)


# R=[]
# for r in range(B):
#     row=[]
#     for c in range(A):
#         row.append(M[c][r])
#     row.reverse()
#     R.append(row)
R=[[M[r][c] for r in range(A-1,-1,-1)]for c in range(B)]
print('R')
print2DList(R)

# L=[]
# for r in range(B-1,0-1,-1):
#     row=[]
#     for c in range(A):
#         row.append(M[c][r])
#     L.append(row)

L=[[M[r][c] for r in range(A)] for c in range(B-1,-1,-1)]
print('L')
print2DList(L)

# T=[]
# for r in range(0,B):
#     row=[]
#     for c in range(A):
#         row.append(M[c][r])
#     T.append(row)

T=[[M[r][c] for r in range(A)]for c in range(0,B)]
print('T')
print2DList(T)