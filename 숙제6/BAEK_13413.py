T = eval(input())

for _ in range(T):
    N = eval(input())
    orig = input()
    goal = input()
    NofBW = 0   #B->W변경 개수
    NofWB = 0   #W->B변경 개수

    for i in range(N):
        if orig[i] == 'B' and goal[i] == 'W':
            NofBW += 1
        elif orig[i] == 'W' and goal[i] == 'B':
            NofWB += 1
    # NofBW=5 , NofWB=2면 2번은 위치바꾸고 3번은 말을 뒤집는다.
    print(max(NofBW,NofWB))
