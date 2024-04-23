from tkinter import *

width = 200
height = 100

class MainGUI:
    def up(self):
        if self.y>5:
            self.canvas.move('ball',0,-5)
            self.y-=5
    def down(self):
        if self.y<height:
            self.canvas.move('ball',0,5)
            self.y+=5
    def left(self):
        if self.x > 5:
            self.canvas.move('ball',-5,0)
            self.x-=5
    def right(self):
        if self.x < width:
            self.canvas.move('ball',5,0)
            self.x+=5
    def __init__(self):
        self.x=10
        self.y=10
        window = Tk()
        window.title('공 옮기기')
        self.canvas = Canvas(window,bg='white',width=width,height=height)
        self.canvas.pack()
        self.canvas.create_oval(self.x,self.y,self.x+10,self.y+10,fill='red',tags='ball')
        frame = Frame(window)
        frame.pack()
        Button(frame,text='상',command=self.up).pack(side=LEFT)
        Button(frame, text='하', command=self.down).pack(side=LEFT)
        Button(frame, text='좌', command=self.left).pack(side=LEFT)
        Button(frame, text='우', command=self.right).pack(side=LEFT)
        window.mainloop()

MainGUI()