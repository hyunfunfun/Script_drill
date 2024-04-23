n = eval(input())
line = input()

M = []
M.append(['.']*n)

r=0
p='.'

for c in range(n):
    if line[c] == '+':
        if p == '/':
            if r==0:
                M.insert(0,['.']*n)
            else:
                r -= 1
        p = M[r][c] = '/'
    elif line[c] == '-':
        if p == '\\' or p == '_':
            if r==len(M)-1:
                M.append(['.']*n)
            r += 1
        p = M[r][c] = '\\'
    else:
        if p == '/':
            if r==0:
                M.insert(0,['.']*n)
            else:
                r -=1
        p = M[r][c] = '_'

for r in range(len(M)):
    for c in range(n):
        print(M[r][c], end='')
    print()