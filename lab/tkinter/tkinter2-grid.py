from tkinter import*
window = Tk()

def process():
    dollar = float(e1.get())
    e2.insert(0,str(dollar*1350))


l1 = Label(window, text='달러',font='helvetica 16 italic')
l2 = Label(window, text='원',font='helvetica 16 italic')
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)


e1 = Entry(window, bg='yellow',fg='black')
e2 = Entry(window, bg='blue', fg='white')
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

b1 = Button(window, text='달러->원',command=process)
b2 = Button(window, text='원->달러')
b1.configure(font='helvetica 12')
b2['bg']='green'
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)

window.mainloop()