file_name = input('파일 이름 입력:')

fp = open(file_name)
s = fp.read()
print('문자',len(s),'개')
print('단어',len(s.split()),'개')
print('행',len(s.split('\n')),'개')
