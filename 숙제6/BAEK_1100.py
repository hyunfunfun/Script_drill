count = 0

# .F.F...F
# F...F.F.
# ...F.F.F
# F.F...F.
# .F...F..
# F...F.F.
# .F.F.F.F
# ..FF..F.

flag = True # T F T F...
for i in range(8):
    b = input() #.F.F...F
    for j in range(8):
        if flag: #참이면 짝수번 인덱스=흰색
            if j%2 == 0 and b[j]=='F':
                count+=1
        else: #홀수번 인덱스=흰색
            if j%2 == 1 and b[j]=='F':
                count +=1
    flag = not flag #줄 바뀔 시 흰색 검은색 교체

print(count)
