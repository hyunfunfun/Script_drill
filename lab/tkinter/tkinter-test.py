from tkinter import *
from random import *
from tkinter.messagebox import *

class MainGUI:
    def refresh(self):
        shuffle(self.deck)
        for i in range(4):
            self.labelList[i]['image'] = self.imageList[self.deck[i]]
    def verify(self):
        fourCards = [self.deck[i] % 13+1 for i in range(4)]
        fourCards.sort()
        expression = self.E.get()
        expression = expression.replace('+',' ')
        expression = expression.replace('-', ' ')
        expression = expression.replace('*', ' ')
        expression = expression.replace('/', ' ')
        expression = expression.replace('(', ' ')
        expression = expression.replace(')', ' ')
        numbers = expression.split()
        numbers = [eval(x) for x in numbers]
        numbers.sort()
        if fourCards == numbers:
            if eval(self.E.get()) == 24:
                showinfo('맞았다!','24점이 됐다')
            else:
                showinfo('틀렸다!',self.E.get()+'는 24점이 아니다')
        else:
            showinfo('틀렸다!','보여지는 카드를 사용해야 합니다.')
    def __init__(self):
        window = Tk()
        window.title('24점 게임')

        self.deck = [x for x in range(52)]
        self.imageList = [PhotoImage(file='image/card/'+str(i)+'.gif') for i in range(1,53)]
        Button(window,text='새로고침',command=self.refresh).pack()
        frame1 = Frame(window)
        frame1.pack()
        self.labelList = []
        for i in range(4):
            self.labelList.append(Label(frame1, image=self.imageList[i]))
            self.labelList[i].pack(side=LEFT)
        self.refresh()
        frame2 = Frame(window)
        frame2.pack()
        Label(frame2,text='수식입력:').pack()
        self.E = Entry(frame2)
        self.E.pack(side=LEFT)
        Button(frame2, text='확인',command=self.verify).pack(side=LEFT)

        window.mainloop()

MainGUI()