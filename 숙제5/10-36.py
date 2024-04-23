from tkinter import *
from random import *
from tkinter.messagebox import *

width = 800
height = 600

class MainGUI:
    def draw(self):
        self.canvas.delete('bar')
        barWidth = (width-20)/20
        Max = 20
        for i in range(20):
            self.canvas.create_rectangle(10+i*barWidth,(height-10)*(1-self.L[i]/(Max+2)),
                                         10+(i+1)*barWidth,height-10,tags='bar')
            self.canvas.create_text(10+i*barWidth+barWidth/2,(height-10)*(1-self.L[i]/(Max+2))-5,
                                    text = str(self.L[i]),tags='bar')
        if self.index >= 0:
            self.canvas.create_rectangle(10+self.index*barWidth,(height-10)*(1-self.L[self.index]/(Max+2)),
                                         10+(self.index+1)*barWidth,height-10,fill='red',tags='bar')
    def reset(self):
        shuffle(self.L)
        self.index = -1
        self.draw()
    def next(self):
        self.index+=1
        self.draw()
        value = int(self.E.get())
        if value == self.L[self.index]:
            showinfo('성공', '찾았다!')
    def __init__(self):
        window = Tk()
        window.title('선형 검색 애니메이션')
        self.canvas = Canvas(window,width=width, height=height, bg='white')
        self.canvas.pack()
        self.L = [x for x in range(1,21)]
        self.reset()

        frame = Frame(window)
        frame.pack()
        Label(frame,text='키입력:').pack(side=LEFT)
        self.E = Entry(frame, width=3, justify=RIGHT)
        self.E.pack(side=LEFT)
        Button(frame, text='다음단계',command=self.next).pack(side=LEFT)
        Button(frame, text='재설정',command=self.reset).pack(side=LEFT)

        window.mainloop()

MainGUI()