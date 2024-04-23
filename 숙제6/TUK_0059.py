P = input() #한줄 postfix 표현식 입력 P='ab+cd+e-a+-'
S = [] #stack
#한문자씩 읽어서 a~z 알파벳이 나오면 스택에 넣는다
#연산자가 나오면 스택에서 2개를 써내서 '('+a+'+'+b+')' 만들어서 스택에 넣는다.

for c in P:
    if c.isalpha():
        S.append(c)
    else:
        b=S.pop()
        a=S.pop()
        S.append('('+a+c+b+')')
E=S.pop()
print(E)