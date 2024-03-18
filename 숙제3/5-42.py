import random
count =0
for i in range(10000000):
    x=random.random()*2.0-1
    y = random.random()*2.0 -1
    if x<0:#1번 영역
        count+=1
    elif 0<=x<=1 and 0<=y<=1:
        slope = -1
        y1 = y - slope*x # (x,y)점을 지나는 y절편
        if y1 <= 1:
            count +=1
print(count)
print('확률:',count/10000000)
