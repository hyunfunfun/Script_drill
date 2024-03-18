x,y = eval(input('x,y좌표 입력:'))

if x>200 or x<0 or y>100 or y<0:
    print('외부')
else:
    slope = -100/200
    # y=slop*x+y1
    y1 = y-slope*x
    if y1<=100:
        print('내부')
    else:
        print('외부')