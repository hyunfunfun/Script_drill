from tkinter import *
import tkinter.ttk

window=Tk()
window.title('노트북')
notebook = tkinter.ttk.Notebook(window,width=800,height=600)
notebook.pack()

frame1 = Frame(window)
notebook.add(frame1,text='페이지1')
Label(frame1,text='페이지1의 내용',fg='red',font='helvetica 48').pack()

frame4 = Frame(window)
notebook.add(frame4,text='페이지1')
Label(frame4,text='페이지1의 내용',fg='blue',font='helvetica 48').pack()

frame4 = Frame(window)
notebook.add(frame4,text='페이지1')
Label(frame4,text='페이지1의 내용',fg='green',font='helvetica 48').pack()

frame4 = Frame(window)
notebook.add(frame4,text='페이지1')
Label(frame4,text='페이지1의 내용',fg='yellow',font='helvetica 48').pack()

window.mainloop()