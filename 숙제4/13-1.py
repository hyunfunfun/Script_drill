file_name = input('파일 이름 입력:')
removeS = input('제거할 문자열 입력:')

fp = open(file_name)
s = fp.read() #파일 전체를 하나의 string으로 읽음
newS = s.replace(removeS,'')
fp.close()

fp = open(file_name,'w')
fp.write(newS)
fp.close()

print('완료')