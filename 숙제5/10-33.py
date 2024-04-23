from tkinter import *
from random import *

width = 800
height = 600

class MainGUI:
    def display(self):
        self.canvas.delete('histogram')
        counts = [0]*26
        for i in range(1000):
            ch = randint(0,25)
            counts[ch] += 1
        barwidth = (width-20)//26
        maxCount = max(counts)
        for i in range(26):
            self.canvas.create_rectangle(10+i*barwidth,height-(height-10)*counts[i]/maxCount,
                                         10+(i+1)*barwidth,height-10,tags='histogram')
            self.canvas.create_text(10+i*barwidth+10,height-5, text=chr(i+ord('a')), tags='histogram')
            self.canvas.create_text(10+i*barwidth+10,height-(height-10)*counts[i]/maxCount-5,
                                    text=str(counts[i]), tags='histogram')
    def __init__(self):
        window=Tk()
        window.title('문자의 개수 세기')
        self.canvas = Canvas(window,width=width,height=height,bg='white')
        self.canvas.pack()
        Button(window,text='히스토그램 출력',command=self.display).pack()
        window.mainloop()
MainGUI()