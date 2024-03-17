def ex():
    point = []
    s = input('6개의 점 입력:')
    points = [eval(i) for i in s.split()]
    for i in range(0,12,2):
        point.append(points[i:i+2])
    print('최하단 점',getRightmostLowestPoint(point))

def getRightmostLowestPoint(points):
    x=points[0][0]
    y=points[0][1]

    for i in range(len(points)):
        if x<points[i][0]:
            x=points[i][0]
        if y>points[i][1]:
            y=points[i][1]
    return x,y

ex()
