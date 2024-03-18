def printChars(ch1, ch2, numberPerLine):
    count = 1 #한줄에 numberPerLine 만큼 출력되는지 제어하는 변수
    start = ord(ch1)
    end = ord(ch2)
    for n in range(start,end+1):
        if count % numberPerLine == 0:
            print(chr(n))
        else:
            print(chr(n), end=' ')
        count += 1

printChars('1','Z',10)