import math

x1,y1 = eval(input('첫 번째 점 : '))
x2,y2 = eval(input('두 번째 점 : '))
d=6370.91*math.acos(math.sin(math.radians(x1)) *
                    math.sin(math.radians(x2)) +
                    math.cos(math.radians(x1)) *
                    math.cos(math.radians(x2)) *
                    math.cos(math.radians(y1-y2)))

print('두 점 사이의 대권거리:',d,'km')