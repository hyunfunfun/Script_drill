N,K = map(eval,input().split())
#1 2 3 4 : 3<4 , 3자리에 다음숫자 넣고 정렬
#1 2 4 3 : 2<4 , 2자리에 다음숫자 넣고 정렬
#1 3 2 4 :

for _ in range(K):
    L=[eval(s) for s in input().split()] #L=[1,3,4,2]
    for i in range(N-1,0,-1):
        if L[i-1] < L[i]:
            R = L[i-1:] #R = [3,4,2]
            R.sort() #R=[2,3,4]
            index = R.index(L[i-1]) # 3의 위치 인덱스
            next = R[index+1] #3다음 숫자 4를 알아낸다
            R.pop(index+1) #3다음 숫자 4를 제거 R = [2,3]
            R.insert(0,next) #4를 제일 앞에 추가 R=[4,2,3]
            L = L[:i-1]+R #새로운 수열 생성 L=[1,4,2,3]
            break
    for n in L:
        print(n,end=' ')
    print()

