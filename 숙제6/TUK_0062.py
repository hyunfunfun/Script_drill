N = eval(input())

D = {} #장르:[플레이횟수, (1등번호,횟수), (2등번호,횟수)]
G = [] #장르 리스트

for i in range(N):
    [genre, play] = input().split()
    play = eval(play)
    if genre in D: #읽은 장르가 D에 있는가?
        D[genre][0] += play # 총 플레이횟수 증가
        if D[genre][1][1] < play: # 해당 장르 1등의 횟수보다 지금읽은 play가 크면
            D[genre][2] = D[genre][1] #현재 1등이 2등으로 내려간다
            D[genre][1] = (i,play) #새로운 (i,play)가 1등으로 등극
        elif D[genre][2][1] < play: #해당 장르 2등의 횟수보다 지금 읽은  play가 크면
            D[genre][2] = (i,play) # 새로운 (i,play)가 2등으로 등극
    else: #D에 없다면
        D[genre] = [play, (i,play), (-1,0)] #새로운 장르를 추가한다

for genre,value in D.items():
    G.append((genre,value[0]))
G.sort(key=lambda x:x[1], reverse=True) #총 재생횟수 기준으로 내림차순 정렬
for i in range(len(G)): #모든 장르별로 두곡씩
    print(D[G[i][0]][1][0]) #해당 장르 1등 번호
    if D[G[i][0]][2][0] != -1: #2등이 있다면
        print(D[G[i][0]][2][0])