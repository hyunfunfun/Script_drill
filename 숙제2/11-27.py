def ex():
    matrix = []
    for i in range(3):
        s = input('3x3행렬의 입력:')
        l = [eval(i) for i in s.split()]
        matrix.append(l)
    print('정렬된 리스트')
    sortColumn(matrix)

def sortColumn(m):
    for i in range(len(m)):
        for j in range(len(m)-1):
            if m[j][i]>m[j+1][i]:
                m[j+1][i],m[j][i] = m[j][i],m[j+1][i]
    a = m
    for x,y,z in a:
        print(x,y,z)

ex()