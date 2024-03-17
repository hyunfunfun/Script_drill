import math

x1,y1 = 35.1768201,126.7735892 # 광주
x2,y2 = 35.1645701,129.0015892 # 부산
x3,y3 = 37.7637326,128.8824475 # 강릉
x4,y4 = 37.565289,126.8491259 # 서울
d1=6370.91*math.acos(math.sin(math.radians(x1)) *
                    math.sin(math.radians(x2)) +
                    math.cos(math.radians(x1)) *
                    math.cos(math.radians(x2)) *
                    math.cos(math.radians(y1-y2)))  #광주  - 부산

d2 = 6370.91*math.acos(math.sin(math.radians(x2)) *
                    math.sin(math.radians(x4)) +
                    math.cos(math.radians(x2)) *
                    math.cos(math.radians(x4)) *
                    math.cos(math.radians(y2-y4)))  #부산  - 서울

d3 = 6370.91*math.acos(math.sin(math.radians(x4)) *
                    math.sin(math.radians(x1)) +
                    math.cos(math.radians(x4)) *
                    math.cos(math.radians(x1)) *
                    math.cos(math.radians(y4-y1)))  #서울  - 광주

d4 = 6370.91*math.acos(math.sin(math.radians(x4)) *
                    math.sin(math.radians(x3)) +
                    math.cos(math.radians(x4)) *
                    math.cos(math.radians(x3)) *
                    math.cos(math.radians(y4-y3)))  #서울  - 강릉



s1 = (d1+d2+d3)/2
s2 = (d2+d3+d4)/2
area = ((s1*(s1-d1)*(s1-d2)*(s1-d3))**0.5) + ((s2*(s2-d2)*(s2-d3)*(s2-d4))**0.5)


area = int(area*10)/10
print("네 도시의 넓이 : ",area)