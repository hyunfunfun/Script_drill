from tkinter import *
class MainGUI:
    def check(self):
        for i in range(6):
            for j in range(4):
                player =self.matrix[i][j]['text']
                if player != ' ' and player ==self.matrix[i][j + 1]['text'] and player ==self.matrix[i][j + 2]['text'] and player ==self.matrix[i][
                    j + 3]['text']:
                    return player
        for i in range(3):
            for j in range(7):
                player =self.matrix[i][j]['text']
                if player != ' ' and player ==self.matrix[i + 1][j]['text'] and player ==self.matrix[i + 2][j]['text'] and player == \
                       self.matrix[i + 3][j]['text']:
                    return player
            # 대각선 검사
        for i in range(3):
            for j in range(4):
                player =self.matrix[i][j]['text']
                if player != ' ' and player ==self.matrix[i + 1][j + 1]['text'] and player ==self.matrix[i + 2][j + 2]['text'] and player == \
                       self.matrix[i + 3][j + 3]['text']:
                    return player
        for i in range(3):
            for j in range(3,7):
                player =self.matrix[i][j]['text']
                if player != ' ' and player ==self.matrix[i + 1][j - 1]['text'] and player ==self.matrix[i + 2][j - 2]['text'] and player == \
                       self.matrix[i + 3][j - 3]['text']:
                    return player
        return ''

    def findRow(self,col):
        for row in range(5, -1, -1):
            if self.matrix[row][col]['text'] == ' ':
                return row
        return 6
    def pressed(self,col):
        row=self.findRow(col)
        if not self.done and self.matrix[row][col]['text']==' ':
            if self.turn:
                self.matrix[row][col]['image'] = self.imageX
                self.matrix[row][col]['text'] = 'X'
            else:
                self.matrix[row][col]['image'] = self.imageO
                self.matrix[row][col]['text'] = 'O'
            self.turn = not self.turn
            if self.check() != '':
                self.done = True
                self.explain.set('플레이어'+self.check()+'이겼습니다.')
            elif self.turn:
                self.explain.set('플레이어 X 차례')
            else:
                self.explain.set('플레이어 O 차례')

    def refresh(self):
        for i in range(6):
            for j in range(7):
                self.matrix[i][j]['image'] = self.imageE
                self.matrix[i][j]['text'] = ' '
        self.done = False
        self.explain.set('플레이어 X 차례')
        self.turn = True
    def __init__(self):
        window = Tk()
        window.title('사목게임')
        frame = Frame(window)
        frame.pack()
        self.matrix = []
        self.imageX = PhotoImage(file='image/x.gif')
        self.imageO = PhotoImage(file='image/o.gif')
        self.imageE = PhotoImage(file='image/empty.gif')
        self.turn = True
        self.done = False
        for i in range(6):
            self.matrix.append([])
            for j in range(7):
                self.matrix[i].append(Button(frame,image=self.imageE,text=' ',\
                                             command=lambda col=j : self.pressed(col)))
                self.matrix[i][j].grid(row=i,column=j)
        frame1 = Frame(window)
        frame1.pack()
        self.explain = StringVar()
        self.explain.set('플레이어 X 차례')
        self.label = Label(frame1,textvariable=self.explain)
        self.label.pack(side=LEFT)
        Button(frame1,text='다시실행',command=self.refresh).pack(side=LEFT)
        window.mainloop()
MainGUI()


