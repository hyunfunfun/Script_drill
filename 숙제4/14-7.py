from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter.messagebox

def openFile():
    filenameRead = askopenfilename()
    filename.set(filenameRead)
def analyze():
    fp = open(filename.get())
    histogram = [0] * 26  #histogram = [0,0,0...]
    S = fp.read() #파일 읽기
    S = S.lower() #소문자 변경
    for c in S: #문자열에서 한 글자씩 가져오기
        if ord('a')<=ord(c)<=ord('z'):
            histogram[ord(c)-ord('a')]+=1
    Max = max(histogram)
    width = int(canvas['width'])
    height = int(canvas['height'])
    barWidth = (width - 20)/26 #하나이 막대 너비 구하기

    for i in range(26): #26개 빈도수
        if histogram[i]:
            canvas.create_rectangle(10+i*barWidth,height - 20 -0.8* height * histogram[i]/Max,
                                    10+(i+1)*barWidth,height-20)
            canvas.create_text(10+i*barWidth+5, height-10,text=chr(ord('a')+i))
            # text.insert(END,chr(ord('a')+i)+'-'+str(histogram[i])+'번 나타납니다.\n')
    fp.close()

window = Tk()
window.title('문자 빈도수 세기')

frame1 = Frame(window)
frame1.pack()

canvas=Canvas(frame1,width=500,height=200)
canvas.pack()

frame2 = Frame(window)
frame2.pack()
Label(frame2, text='파일명 입력:').pack(side=LEFT)
filename = StringVar()
Entry(frame2, width=20, textvariable=filename).pack(side=LEFT)
Button(frame2, text='열기', command=openFile).pack(side=LEFT)
Button(frame2, text='결과보기', command=analyze).pack(side=LEFT)
window.mainloop()