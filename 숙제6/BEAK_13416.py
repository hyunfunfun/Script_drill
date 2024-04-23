T=eval(input())

for _ in range(T):
    N = eval(input())
    profit = 0  #주식투자 이윤
    for i in range(N):
        L = [eval(s) for s in input().split()]
        M = max(L)
        if M>0:
            profit += M
    print(profit)
