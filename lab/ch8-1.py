import sys
print('welcome to','python',sep='~',end='!',file=sys.stderr)

f=open('ch8-1.txt','w')
print('file write',file=f)
f.close()

