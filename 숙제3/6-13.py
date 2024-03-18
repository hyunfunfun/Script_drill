#m(n) = 1/2+2/3 ... + (n-1)/n + n/(n+1)  =  m(n-1)+n/(n+1)
def m(n):
    if n==1:
        return 1/2
    else :
        return m(n-1)+n/(n+1)

print('i','\t','m(i)')
for i in range(1,21):
    print(i,'\t',m(i))
