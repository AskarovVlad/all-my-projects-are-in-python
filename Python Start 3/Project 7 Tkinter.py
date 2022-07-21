def hello():
    print("Hello")

from tkinter import *

tk = Tk()
btn = Button(tk, text='Нажми на меня', command=hello)
btn.pack()

from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()

from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_rectangle(10, 10, 50, 50)
import random   # создает рандомные числа
from tkinter import *
# colorchooser.askcolor()     # спросить цвет заливки
# 359 градусов полный круг
# Polygon — многоугольник
# Outline — контур
# Black — черный
# Create_text — создать текст

import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
for x in range(0, 60):
# canvas.move(1, 5, 3) двигает наш рисунок 1 - идентификатор рисунка, 5 - на 5 пикселей вправо, 3 - на 3 пикс вниз
# если добавить минус -5 то влево и -3 вверх
# tk.update() принудительное обновление расположения рисунка с каждым выполнением цикла, без него рисунок окажется в конце
# time.sleep(0.05)
def movetriangle(event):
# canvas.move(1, 5, 0)
canvas.bind_all('<KeyPress-Return>', movetriangle)
