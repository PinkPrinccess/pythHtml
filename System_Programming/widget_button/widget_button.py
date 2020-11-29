from tkinter import *

root = Tk()
label1 = Label(width=15)
color = Entry(text='Код цвета', width=15)
color.insert(0, 'Код цвета')
label1['text'] = 'Цвет'

def vv1():
    color.delete(0, END)
    color.insert(0, "#ff0000")
    label1['text'] = 'Красный'
def vv2():
    color.delete(0, END)
    color.insert(0, "#ff7d00")
    label1['text'] = 'Оранжевый'
def vv3():
    color.delete(0, END)
    color.insert(0, "#ffff00")
    label1['text'] = 'Жёлтый'
def vv4():
    color.delete(0, END)
    color.insert(0, "#00ff00")
    label1['text'] = 'Зелёный'
def vv5():
    color.delete(0, END)
    color.insert(0, "#007dff")
    label1['text'] = 'Голубой'
def vv6():
    color.delete(0, END)
    color.insert(0, "#0000ff")
    label1['text'] = 'Синий'
def vv7():
    color.delete(0, END)
    color.insert(0, "#7d00ff")
    label1['text'] = 'Фиолетовый'

button1 = Button(bg='#ff0000', command=vv1, width=15,)
button2 = Button(bg='#ff7d00', command=vv2, width=15)
button3 = Button(bg='#ffff00', command=vv3, width=15)
button4 = Button(bg='#00ff00', command=vv4, width=15)
button5 = Button(bg='#007dff', command=vv5, width=15)
button6 = Button(bg='#0000ff', command=vv6, width=15)
button7 = Button(bg='#7d00ff', command=vv7, width=15)
label1.pack()
color.pack()
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
root.mainloop()
