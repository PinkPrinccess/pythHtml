from tkinter import *
from tkinter import messagebox

global a, b

def func():
    try:
        global a, b
        a = ent.get()
        a = int(a)
        b = ent1.get()
        b = int(b)
    except ValueError:
        messagebox.showerror("ОШИБКА", "Введите корректные значения")

def summa():
    func()
    s = a+b
    s = str(s)
    tab['text'] = ' '.join(s)

def minus():
    func()
    s = a-b
    s = str(s)
    tab['text'] = ' '.join(s)

def multcup():
    func()
    s = a*b
    s = str(s)
    tab['text'] = ' '.join(s)

def divAll():
    func()
    s = a/b
    s = str(s)
    tab['text'] = ' '.join(s)

root = Tk()

sub = Entry(width=15)
sub1 = Entry(width=15)
buss = Button(text="+", width=15)
buss2 = Button(text="-", width=15)
buss3 = Button(text="*", width=15)
buss4 = Button(text="/", width=15)
tab = Label(width=20, bg='black', fg='white')


buss.bind('<Button-1>', summa)
buss2.bind('<Button-1>', minus)
buss3.bind('<Button-1>', multcup)
buss4.bind('<Button-1>', divAll)

sub.pack()
sub1.pack()
buss.pack()
buss2.pack()
buss3.pack()
buss4.pack()
tab.pack()
root.mainloop()
